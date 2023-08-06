# -*- coding: utf-8 -*-
import json
import os
import pytest
from _pytest.nodes import Item
from common.db.handle_db import MysqlDB
from loguru import logger
from common.plat.jira_platform import JiraPlatForm
from common.config.config import LOG_PATH_FILE, TEST_PATH, TEST_TARGET_RESULTS_PATH, TEST_TARGET_REPORT_PATH,TEST_UI_PATH
from common.data.handle_common import get_system_key,format_caseName,print_info
from common.file.handle_system import del_file
from common.common.constant import Constant
from common.data.data_process import DataProcess
from common.plugin.data_plugin import DataPlugin
from common.plugin.data_bus import DataBus
from common.plat.ATF_platform import ATFPlatForm
from common.plugin.atf_plugin import ATFPlugin
from os import path


class PytestPlugin(object):

    @classmethod
    def getCaseNameList(self):
        """
        获取用例列表
        """
        logger.info("获取测试用例和测试脚本")
        case_name_list = []
        if DataProcess.isNotNull(get_system_key(Constant.TEST_CASE_NAME_LIST)):
            case_name_list = ATFPlatForm.getCycleByCaseName(get_system_key(Constant.TEST_CASE_NAME_LIST))
        else:
            if DataProcess.isNotNull(get_system_key('Result')):
                case_name_list = ATFPlatForm.getCycleByResult(get_system_key('Result'))
            else:
                case_name_list = ATFPlatForm.getCycleByResult()
        PytestPlugin.initRunCyleCase(case_name_list)
        return case_name_list

    @classmethod
    def insertCaseToPlan(self):
        if DataProcess.isNotNull(get_system_key('addCaseJql')) and DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)):
            JiraPlatForm.saveCaseToTestPlanByJql(get_system_key('issueKey'),get_system_key('addCaseJql'))

    @classmethod
    def runsingleCase(self):
        single_case_path = os.path.join(TEST_PATH, 'test_single')
        logger.info("开始执行单场景脚本:" + single_case_path)
        pytest.main(
            args=['-v', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning', single_case_path,
                  f'--alluredir={TEST_TARGET_RESULTS_PATH}'])
        logger.info("单场景脚本成功:" + single_case_path)

    @classmethod
    def runPathCase(self, _path):
        _pathlist = _path.split(',')
        for _path in _pathlist:
            case_path = os.path.join(TEST_PATH, _path)
            logger.info("开始执行脚本的路径:" + case_path)
            pytest.main(
                args=['-v', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning', case_path,
                      f'--alluredir={TEST_TARGET_RESULTS_PATH}'])
            logger.info("执行脚本成功:" + case_path)

    @classmethod
    def runSceneCase(self, _caseNameList):
        _list = []
        _config = {'key':'traffic','env':'test'}
        _mysql = MysqlDB(_config)
        for caseName in _caseNameList:
            caseName = format_caseName(caseName['casename'])
            _sql = f"select distinct(caseurl) from test_autotest_script,test_autotest_run where  test_autotest_run.casename=test_autotest_script.testname " \
                   f"and test_autotest_run.casename ='{caseName}' and test_autotest_run.`status`='自动化执行'"
            _list = _mysql.execute(_sql).fetchall()
            if len(_list) > 0:
                caseUrl = str(_list[0]['caseurl']).replace("(", "").replace(")", "")
                _scriptPath = path.join(get_system_key(Constant.CURRENT_PATH), caseUrl, )
                logger.info(f"---------开始执行脚本用例名称：{caseName}  脚本路径:{_scriptPath}-------------")
                pytest.main(
                    args=['-v', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning', _scriptPath,
                          f'--alluredir={TEST_TARGET_RESULTS_PATH}'])
                logger.info("----------执行脚本成功---------------")
            else:
                logger.info(f'-----------用例名称:{caseName} SQL语句：{_sql} 没有发现可执行脚本-------------')
        _mysql.close()

    @classmethod
    def initRunCyleCase(self, _caseNameList):
        if get_system_key(Constant.Jenkins_RESULT) != "'"+Constant.STATUS_AUTOTEST+"'".strip():
            ATFPlatForm.syncCaseJiraMysql(_caseNameList, Constant.STATUS_AUTOTEST)



    @classmethod
    def pytest_run_case(cls, _deleteResult:bool= True):
        """
        运行自动化用例
        :return:
        """
        if DataProcess.isNotNull(get_system_key('addCaseJql')) and DataProcess.isNotNull(
                get_system_key(Constant.ISSUE_KEY)):
            JiraPlatForm.saveCaseToTestPlanByJql(get_system_key(Constant.ISSUE_KEY), get_system_key('addCaseJql'))
        else:
            DataBus.save_init_data()
            ATFPlatForm.syncCycleNameCase()
            DataBus.run_info()
            logger.add(LOG_PATH_FILE, enqueue=True, encoding='utf-8')
            if _deleteResult:
                del_file(TEST_TARGET_RESULTS_PATH)
            if DataProcess.isNotNull(get_system_key(Constant.TEST_CASE_PATH)):
                _caseNameList = PytestPlugin.getCaseNameList()
                if len(_caseNameList) == 0:
                    logger.info("无测试用例列表可运行，运行默认的测试集")
                    PytestPlugin.runPathCase(get_system_key(Constant.TEST_CASE_PATH))
                else:
                    PytestPlugin.runsingleCase()
                    PytestPlugin.runSceneCase(_caseNameList)



    @classmethod
    def allure_report(cls):
        """
        生成测试报告
        :return:
        """

        if get_system_key(Constant.ALLURE_PATH) is not None:
            ALLURE_PATH = get_system_key(Constant.ALLURE_PATH)
        else:
            ALLURE_PATH = ''
        if get_system_key(Constant.RUN_TYPE) is None or get_system_key(Constant.RUN_TYPE) != 'jenkins' or get_system_key(Constant.RUN_TYPE) == '':
            os.system(f'{ALLURE_PATH}allure generate {TEST_TARGET_RESULTS_PATH} -o {TEST_TARGET_REPORT_PATH} --clean')
            logger.success('Allure测试报告已生成')
        ATFPlugin.sendResult()


    @classmethod
    def change_allure_title(cls,report_html_path: str = TEST_TARGET_REPORT_PATH):
        """
        修改Allure标题
        :param name: 
        :param report_html_path: 
        :return: 
        """
        dict = {}
        # 定义为只读模型，并定义名称为f
        with open(f'{report_html_path}/widgets/summary.json', 'rb') as f:
            # 加载json文件中的内容给params
            params = json.load(f)
            # 修改内容
            params['reportName'] = get_system_key("JOB_NAME")
            # 将修改后的内容保存在dict中
            dict = params
            logger.info("修改测试报告名称：" + get_system_key(Constant.PROJECT_NAME))
            with open(f'{report_html_path}/widgets/summary.json', 'w', encoding="utf-8") as r:
                # 将dict写入名称为r的文件中
                json.dump(dict, r, ensure_ascii=False, indent=4)

            # 关闭json读模式
            f.close()
            logger.info("修改测试报告完成")

    @classmethod
    def generated_code(self, _url: str = '', _path: str = TEST_UI_PATH):
        if not DataProcess.isNotNull(_url):
            _url = get_system_key('url')
        # test_case_dir = '{}{}'.format(os.getcwd(), _path)
        test_case_dir = '{}'.format(_path)
        file_list = [os.path.join(test_case_dir, file) for file in os.listdir(test_case_dir) if "test_" in file]
        test_case_num = len(file_list) - 2
        print("{}目录下存在{}测试用例".format(test_case_dir, test_case_num))
        cmd = r"python -m playwright codegen --target pytest -o {}/test_{}.py -b chromium {}". \
            format(_path, str(test_case_num + 1).zfill(3), _url)
        print("执行录制测试用例命令：{}".format(cmd))
        os.system(cmd)

    @classmethod
    def pytest_case_meta(self, item: Item):
        _caseTitle, _caseNo = PytestPlugin.getCaseName(item)
        logger.info(f"----------开始执行用例名称：{_caseTitle}  用例编号:{_caseNo}-----------")
        DataPlugin.jira_convert_allure(_caseTitle,_caseNo)

    @classmethod
    def getCaseName(self, item: Item):
        _caseTitle = "脚本未设置用例名称"
        _caseNo = "00000"
        _caseData = ""
        try:
            parmkes = item._pyfuncitem.callspec.indices.keys()
            if DataProcess.isNotNull(parmkes):
                _caseTitle = item._pyfuncitem.callspec.params[list(parmkes)[0]].get(Constant.CASE_TITLE)
                _caseNo = item._pyfuncitem.callspec.params[list(parmkes)[0]].get(Constant.CASE_NO)
                _caseData = item._pyfuncitem.callspec.params[list(parmkes)[0]]
        except Exception as e:
            print_info('未通过Excel获取到用例信息')
        try:
            _caseTitle = item.__dict__['keywords'].__dict__['_markers']['__allure_display_name__']
        except Exception as e:
            print_info('未通过装饰器title获取到用例信息')
        try:
            _caseNo = item.__dict__['keywords'].__dict__['_markers']['pytestmark'][0].__dict__['args']
            if str(_caseNo).find("(")>-1:
                _caseNo = '00000'
        except Exception as e:
            print_info('未通过装饰器ID获取到用例信息')
        print_info(f"执行用例名称：{_caseTitle} 用例编号:{_caseNo}")
        print_info(f'用例数据:{_caseData}')
        return _caseTitle, _caseNo

    @classmethod
    def send_case_result(self, item: Item, result):
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                get_system_key(Constant.TEST_SRTCYCLE_ID)):
            _caseTitle, _caseNo = PytestPlugin.getCaseName(item)
            logger.info(f"-----------执行用例完成名称：{_caseTitle}  用例编号:{_caseNo}  结果:{result} -----------")
            if result != 'skipped':
                _caseTitleList = _caseTitle.split(';')
                for temp in _caseTitleList:
                    ATFPlatForm.sent_result_byCaseName(temp, _caseNo, result, "")


if __name__ == '__main__':
    id_list_in = {'菜单管理：删除菜单后，角色管理中，选中某一角色后，右侧菜单列表不展示该菜单信息','新增角色，勾选菜单列表，再取消勾选查看关联关系'}
    sql = f"select distinct(caseurl) from test_autotest_script where `status` = '0'"
    sql += " and testname in (%s)" % ','.join(["'%s'" % testname for testname in id_list_in])
