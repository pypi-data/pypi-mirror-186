import os
from loguru import logger
import json
from common.common.api_driver import APIDriver
from common.common.constant import Constant
from common.data.handle_common import get_system_key,format_caseName,set_system_key,print_info
from common.plat.mysql_platform import MysqlPlatForm
from common.plat.jira_platform import JiraPlatForm
from common.data.data_process import DataProcess
from common.db.handle_db import MysqlDB
import datetime


class ATFPlatForm(object):

    @classmethod
    def db_ops(self, _key, _sql, env: str = Constant.ENV):
        """
        执行SQL操作
        :param _key:
        :param _sql:
        :param env:
        :return:
        """
        _sqltemp=_sql.encode("utf-8").decode("latin1")
        if get_system_key(env) is not None:
            env = get_system_key(env)
        sql_type = _sql.strip().split(" ")[0].lower()
        if "select" == sql_type:
            _tempdata = APIDriver.http_request(url=f"{Constant.ATF_URL_API}/querySetResult/{_key}/{env}",
                                               method='post', parametric_key='data', data=_sqltemp
                                               )
            logger.info(f"执行sql成功:{_sql}")
            return list(_tempdata.json())
        if "insert" == sql_type or "delete":
            _tempdata = APIDriver.http_request(url=f"{Constant.ATF_URL_API}/doExecute/{_key}/{env}",
                                               method='post', parametric_key='data', data=_sqltemp)
            logger.info(f"执行sql成功:{_sql}")
            return _tempdata.text
        else:
            logger.error("不支持其他语句类型执行，请检查sql")


    @classmethod
    def runDeploy(self,jobName, _pramater):
        """
        推送测试结果
        :param jobName:
        :param _pramater:
        :return:
        """
        _tempdata = APIDriver.http_request(url=f"{Constant.ATF_URL}/jenkins/runDeploy/{jobName}",
                                               method='get', parametric_key='params', data=_pramater)
        return _tempdata


    @classmethod
    def getProjectData(self, projectName, projectKey):
        """
        获取项目数据
        :param projectName: 项目别名
        :param projectKey: 关键词
        :return:
        """

        try:
            content = APIDriver.http_request(url=f"{Constant.ATF_URL}/api/getProjectData/{projectName}/{projectKey}",
            method='get')
            return (json.loads(content.content)["data"]["projectValue"])
        except Exception as e:
            logger.info(f"{Constant.ATF_URL}/api/getProjectData/{projectName}/{projectKey}" + "获取不到value")
            return None

    @classmethod
    def setProjectData(self, projectKey, value, type = 1):
        """
        设置项目数据
        :param projectName: 项目别名
        :param projectKey: 关键词
        :param value: 值
        :param type: 数据类型[0可以重复使用，1不可以重复使用]
        :return:
        """
        if get_system_key('ProjectAlice') is not None and get_system_key('ProjectAlice').strip() != '':
            projectName = get_system_key('ProjectAlice')
            return APIDriver.http_request(
                url=f"{Constant.ATF_URL}/api/setProjectData/{projectName}/{projectKey}/{value}/{type}",
                method='get'
                )

    @classmethod
    def getCycleByCaseName(self, CaseName:str):
        _list = []
        try:
            _listCase = CaseName.split(";")
            if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
                for _temp in _listCase:
                    _dict =MysqlPlatForm.get_test_case_info(get_system_key(Constant.ISSUE_KEY), get_system_key(Constant.TEST_SRTCYCLE_ID), format_caseName(_temp))
                    if len(_dict) > 0:
                        _list.append(_dict[0])
        except Exception as e:
            logger.info(f'获取周期的用例名称{CaseName}信息异常' + repr(e))
        return _list

    @classmethod
    def updateCycleByCaseRunID(self, runID, result):
        _list = []
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                get_system_key(Constant.TEST_SRTCYCLE_ID)):
            MysqlPlatForm.update_test_case_info_ByRunID(get_system_key(Constant.ISSUE_KEY),get_system_key(Constant.TEST_SRTCYCLE_ID),runID,result)
        return _list

    @classmethod
    def syncCaseJiraMysql(self, _caseNameList, result):
        logger.info("初始化需要运行的测试用例并同步到数据库")
        try:
            _config = {'key':'traffic','env':'test'}
            _mysql = MysqlDB(_config)
            for _case in _caseNameList:
                jira_key, case_name, case_link, case_priority, case_model, case_suit, case_story_id, case_story_name, case_story_link, cast_type = \
                    JiraPlatForm.getCaseInfo(_case['caseid'])
                #只更新执行方式为自动化的用例
                if cast_type == Constant.CASE_TYPE_AUTO:
                    caserunid = _case['caserunid']
                    _sql = f"update `traffic_test`.`test_autotest_run` SET `status` = '{result}' where caserunid='{caserunid}'"
                    try:
                        JiraPlatForm.updatecaseByrunId(_case['caserunid'], result, '')
                        _mysql.execute(_sql).fetchall()
                    except Exception as e:
                        logger.info(f'初始化用例：{caserunid}  状态: {result} SQL语句:{_sql} 异常信息:' + repr(e))
            _mysql.close()
        except Exception as e:
            logger.info(f'初始化用例列表：{_caseNameList}异常' + repr(e))

    @classmethod
    def insert_test_autotest_script(self, testname, caseurl):
        if DataProcess.isNotNull(get_system_key(Constant.GIT_PROJECTNAME)):
            _config = {'key': 'traffic', 'env': 'test'}
            testname = format_caseName(testname)
            gitname = get_system_key(Constant.GIT_PROJECTNAME)
            _mysql = MysqlDB(_config)
            sql = f"select distinct(caseurl) from test_autotest_script where `status` = '0' and gitname ='{gitname}' and testname='{testname}' and caseurl='{caseurl}'"
            _list = _mysql.execute(sql).fetchall()
            if _list is None or _list.__len__() < 1:
                _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                caseArr = str(caseurl).split('::')
                scripturl = f'http://172.28.22.90/autotest/{gitname}/-/blob/master/{caseArr[0]}'
                scriptclass = caseArr[1]
                scriptmethod = caseArr[2]
                scriptname = get_system_key(Constant.CURRENT_PATH)+os.sep+caseArr[0]
                _sql = f"INSERT INTO `traffic_test`.`test_autotest_script`(`gitname`, `suitname`, `tagversion`, `testname`, `scriptclass`, `scriptmethod`, `scriptname`, `scriptpackage`, `status`, `updatetime`, `caseurl`, `scripturl`) " \
                       f"VALUES ('{gitname}', '', 'run', '{testname}', '{scriptclass}', '{scriptmethod}', '{scriptname}', '', '0', '{_date}', '{caseurl}', '{scripturl}')"
                _mysql.execute(_sql)
            _mysql.conn.commit()
            _mysql.close()

    @classmethod
    def get_test_autotest_run_byStatus(self, result):
        _list = []
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                get_system_key(Constant.TEST_SRTCYCLE_ID)):
            _list = MysqlPlatForm.get_test_autotest_run(get_system_key(Constant.ISSUE_KEY),
                                                        get_system_key(Constant.TEST_SRTCYCLE_ID), result)
        return _list

    @classmethod
    def getCycleByCaseID(self, caseId: str):
        _list = []
        try:
            _listCase = caseId.split(";")
            if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                    get_system_key(Constant.TEST_SRTCYCLE_ID)):
                for _temp in _listCase:
                    _dict = MysqlPlatForm.get_test_case_info_ByID(get_system_key(Constant.ISSUE_KEY),
                                                             get_system_key(Constant.TEST_SRTCYCLE_ID),
                                                             _temp)
                    if len(_dict) > 0:
                        _list.append(_dict[0])
        except Exception as e:
            logger.info(f'获取周期的用例编号{caseId}信息异常'+repr(e))
        return _list

    @classmethod
    def getCycleByResult(self,  restult: str = "'通过','未执行','失败','自动化执行'"):
        _list = []
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                get_system_key(Constant.TEST_SRTCYCLE_ID)):
            _list = MysqlPlatForm.get_test_autotest_run(get_system_key(Constant.ISSUE_KEY),
                                                         get_system_key(Constant.TEST_SRTCYCLE_ID),
                                                         restult)
        return _list

    @classmethod
    def runSenceCase(self, _caseList):
        _caseNameList = []
        _caseScriptList = []
        for caseName in _caseNameList:
            caseName = format_caseName(caseName['casename'])
            _caseNameList.append(caseName)
        _caseScriptList = MysqlPlatForm.getScriptyPathByCaseNameList(_caseNameList)
        return _caseNameList, _caseScriptList


    @classmethod
    def sent_result_byCaseName(self, CaseName, CaseID, result, comment):
        try:
            _case = ATFPlatForm.getCycleByCaseName(CaseName)
            if len(_case) == 0 and DataProcess.isNotNull(CaseID):
                _case = ATFPlatForm.getCycleByCaseID(CaseID)
            if len(_case) > 0:
                _runid = _case[0]['caserunid']
                JiraPlatForm.updatecaseByrunId(_runid, result, comment)
                if comment == "":
                    ATFPlatForm.updateCycleByCaseRunID(_runid, result)
                logger.info(f'用例名称:{CaseName} 运行ID：{_runid}  结果:{result} 结果描述:{comment} 推送成功')
            else:
                logger.info(f'用例名称:{CaseName} 用例编号:{CaseID} 结果:{result} 在测试周期中没有找到')
        except Exception as e:
            logger.info(f'用例名称:{CaseName} 用例编号:{CaseID} 结果:{result}  结果描述:{comment} 推送异常:' + repr(e))

    @classmethod
    def syncCycleNameCase(self):
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            testPlanIssueKey = get_system_key(Constant.ISSUE_KEY)
            testPlanID = json.loads(JiraPlatForm.getJiraIssueInfo(f'{get_system_key(Constant.ISSUE_KEY)}?fields=id').content)['id']
            set_system_key(Constant.TEST_TestPlan_ID, testPlanID)
            cycleId = get_system_key(Constant.TEST_SRTCYCLE_ID)
            cycleInfo = JiraPlatForm.getCycleInfoByTestPlanIssueKey(testPlanIssueKey, cycleId)
            set_system_key(Constant.TEST_SRTCYCLE_NAME, cycleInfo['name'])
            set_system_key(Constant.ISSUE_KEY, testPlanIssueKey)
            set_system_key(Constant.TEST_SRTCYCLE_ID, cycleId)
            _caselist = JiraPlatForm.getReclyTestCase(get_system_key(Constant.ISSUE_KEY), get_system_key(Constant.TEST_SRTCYCLE_NAME))
            MysqlPlatForm.sync_mysql_data(_caselist)



if __name__ == '__main__':
    os.environ[Constant.TEST_SRTCYCLE_NAME] = 'P0冒烟测试'
    os.environ[Constant.ISSUE_KEY] = 'DQ21207-163'
    os.environ[Constant.JIRA_USERNAME] ='oushiqiang'
    os.environ[Constant.JIRA_PASSWORD] ='Xiaoshu406@@'
    _caselist = JiraPlatForm.getReclyTestCase(get_system_key(Constant.ISSUE_KEY),
                                              get_system_key(Constant.TEST_SRTCYCLE_NAME))
    MysqlPlatForm.sync_mysql_data(_caselist)