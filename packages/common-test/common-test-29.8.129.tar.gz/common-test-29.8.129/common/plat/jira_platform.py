import json
import os
import re
from jsonpath import jsonpath

from common.common.api_driver import APIDriver
from common.data.handle_common import get_system_key, set_system_key
from common.common.constant import Constant
from requests.auth import HTTPBasicAuth
from common.data.data_process import DataProcess
from loguru import logger

class JiraPlatForm(object):

    @classmethod
    def getJiraIssueInfo(self, jira_no):
        """
        通过Jira号获取jira信息
        :param jira_no:
        :return:
        """

        return APIDriver.http_request(url=f"{Constant.JIRA_URL}/rest/api/latest/issue/{jira_no}",method='get',
                                        _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),get_system_key(Constant.JIRA_PASSWORD))
                                      )

    @classmethod
    def getReclyTestCase(self, testPlanIssueKey, cycleName):
        logger.info(f"获取测试计划{testPlanIssueKey}周期名称{cycleName}用例信息")
        content = APIDriver.http_request(url=f"{Constant.JIRA_URL}/rest/synapse/latest/public/testPlan/{testPlanIssueKey}/cycle/{cycleName}/testRuns", method='get',
                                      _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                                          get_system_key(Constant.JIRA_PASSWORD))
                                        )
        try:
            content = json.loads(re.sub("&ldquo;|&rdquo;","", content.content.decode('gbk')))
        except UnicodeDecodeError as e:
            content = json.loads(re.sub("&ldquo;|&rdquo;","", content.content.decode('utf-8')))
        return content

    @classmethod
    def updateBatchRunID(self,runidList, result_temp):
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            CycleId=get_system_key(Constant.TEST_SRTCYCLE_ID)
            testPlanIssueKey=get_system_key(Constant.ISSUE_KEY)
            result = 4
            if result_temp == 'passed':
                result = 1
            if result_temp == 'failed':
                result = 2
            if result_temp == '未执行':
                result = 4
            try:
                _dict={"testCycleId":CycleId,"status":"result","runIds":runidList}
                APIDriver.http_request(
                    url=f"{Constant.JIRA_URL}/rest/synapse/latest/public/testPlan/{testPlanIssueKey}/bulkStatusUpdate",
                    method='post',
                    parametric_key='json',
                    data=_dict,
                    _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                        get_system_key(Constant.JIRA_PASSWORD)),
                )
            except Exception as e:
                logger.info(f'用例运行ID：{runidList}  结果:{result} 推送异常：{e}')

    @classmethod
    def updatecaseByrunId(self, runid, temp, comment):
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            result = 4
            if temp == 'passed':
                result = 1
            if temp == 'failed':
                result = 2
            if temp == 'broken':
                result = 7
            if temp == '未执行':
                result = 4
            if temp == '自动化执行':
                result = 6
            try:
                if JiraPlatForm._isNotNull(temp):
                    APIDriver.http_request(
                        url=f"{Constant.JIRA_URL}/rest/synapse/1.0/testRun/updateTestRunStatus?runId={runid}&status={result}",
                        method='put',
                        parametric_key='json',
                        _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                            get_system_key(Constant.JIRA_PASSWORD))
                    )
                if JiraPlatForm._isNotNull(comment):
                    APIDriver.http_request(
                        url=f"{Constant.JIRA_URL}/rest/synapse/1.0/testRun/updateTestRunComment",
                        method='put',
                        parametric_key='json',
                        data=json.loads('{"testRunId":_runId,"testRunComment":"_comment"}'.replace('_runId', str(runid)).replace('_comment',comment)),
                        _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                            get_system_key(Constant.JIRA_PASSWORD))
                    )
            except Exception as e:
                logger.info(f'用例运行ID：{runid}  结果:{result}  结果描述:{comment}  推送异常：{e}')



    @classmethod
    def setJiraFlowStatus(self, flow_id):
        """
                触发工作流程
                :param jira_key: Jira_key
                :param flow_id: 流程ID
                :return:
                """
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)):
            jira_key =get_system_key(Constant.ISSUE_KEY)
            logger.info(f'更新{jira_key}工作流状态')
            return APIDriver.http_request(url=f"{Constant.JIRA_URL}/rest/api/2/issue/{jira_key}/transitions?expand=transitions.fields",
                                          method='post',
                                          parametric_key='json',
                                          data=json.loads('{"transition":{"id":"flow_id"}}'.replace('flow_id',flow_id)),
                                          _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                                              get_system_key(Constant.JIRA_PASSWORD))
                                          )
        else:
            return "no issue key"

    @classmethod
    def setJiraComment(self, comment):
        """
        添加Jira的备注
        :param jira_key:
        :param comment:
        :return:
        """
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)):
            jira_key = get_system_key(Constant.ISSUE_KEY)
            return APIDriver.http_request(url=f"{Constant.JIRA_URL}/rest/api/2/issue/{jira_key}/comment",
                                          method='post',
                                          parametric_key='json',
                                          data=json.loads('{"body":"comment"}'.replace('comment',comment)),
                                          _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME),
                                                            get_system_key(Constant.JIRA_PASSWORD))
                                         )
        else:
            return "no issue key"

    @classmethod
    def getJiraIssueSummer(self, case_name):
        jira_no = get_system_key(Constant.CASE_NAME_NO_FIX+case_name)
        _link = f'{Constant.JIRA_URL}/browse/{jira_no}'
        return case_name, _link, jira_no


    @classmethod
    def getJiraTestCaseKey(self, case_name, jira_key):
        """
        通过项目id和测试用例名，获取测试用例的链接：
        例如：
        """
        try:
            project_id = get_system_key(Constant.PROJECT_NAME).split("（")[-1].split("）")[0]
            jql = "summary ~  %s AND project in (%s) AND issuetype = 测试用例 AND 用例执行方式 = 自动化" % (str(case_name), str(project_id))
            fields = ["id", "key", "summary"]
            content = JiraPlatForm.getDataByJql(jql, fields)
            for item in content["issues"]:
                if item["fields"]["summary"].strip() == str(case_name).strip():
                    jira_key = item['key']
                    set_system_key(Constant.CASE_NAME_NO_FIX+case_name, jira_key)
        except Exception as e:
            logger.info(f'通过用例名称获取用例key失败: \n用例名：%s' % str(case_name))
            set_system_key(Constant.CASE_NAME_NO_FIX + case_name, jira_key)
        return jira_key

    @classmethod
    def getCaseInfo(self, jira_key):
        try:
            case_link = f'{Constant.JIRA_URL}/browse/'
            case_priority = "P1"
            case_model = "未关联用例模块"
            case_name = "未关联用例名称"
            case_suit = "未关联测试集"
            case_type = "手工"
            case_story_id = ""
            case_story_name = "未关联需求名称"
            case_story_link = f'{Constant.JIRA_URL}/browse/'
            content = json.loads(JiraPlatForm.
                                 getJiraIssueInfo(jira_key+'?fields=summary,customfield_14901,customfield_11758,customfield_10300,customfield_10301,customfield_14903')
                                 .content)['fields']
            case_link = f'{Constant.JIRA_URL}/browse/{jira_key}'
            case_name = content['summary']
            if JiraPlatForm._isNotNull(content['customfield_14901']):
                case_priority = content['customfield_14901']['value']
            if JiraPlatForm._isNotNull(content['customfield_11758']):
                case_model = content['customfield_11758']['value']
            if JiraPlatForm._isNotNull(content['customfield_10300']):
                case_suit = content['customfield_10300']
            if JiraPlatForm._isNotNull(content['customfield_10301']):
                case_story_id_list = content['customfield_10301']
                if JiraPlatForm._isNotNull(str(case_story_id_list).replace("\t","").strip()):
                    case_story_id = str(case_story_id_list.split(",")[0]).replace("\t","").strip()
                    case_story_link = f'{Constant.JIRA_URL}/browse/{case_story_id}'
                    case_story_name = json.loads(JiraPlatForm.getJiraIssueInfo(case_story_id+'?fields=summary').content)['fields']['summary']
            if JiraPlatForm._isNotNull(content['customfield_14903']):
                case_type = content['customfield_14903']['value']
        except Exception as e:
            logger.info(f'获取用例key用例信息失败，用例的Key:{jira_key}')
        return jira_key, case_name, case_link, case_priority, case_model, case_suit, case_story_id, case_story_name, case_story_link, case_type

    @classmethod
    def _isNotNull(self, data):
        try:
            if data is None:
                return False
            if isinstance(data, str):
                _data = data
            else:
                _data = str(data)
            if _data.strip() == '':
                return False
            else:
                return True
        except Exception as e:
            logger.info('判断数据是否为空异常,数据：' + data)
            return True

    @classmethod
    def getCaseNameListFromCircleId(self, result=""):
        """
        通过Jira的测试计划number，测试周期名字，来获取测试用例列表
        :param jira_no: 测试计划number
        :param cycle_id: 测试周期id
        :param result: 测试用例执行结果进行筛选（通过，失败，未执行等）
        :return:
        """
        case_name_list=[]
        if DataProcess.isNotNull(get_system_key(Constant.ISSUE_KEY)) and DataProcess.isNotNull(
                get_system_key(Constant.TEST_SRTCYCLE_ID)):
            jira_no = get_system_key(Constant.ISSUE_KEY)
            cycle_id = get_system_key(Constant.TEST_SRTCYCLE_ID)
            content = APIDriver.http_request(
                url=f"{Constant.JIRA_URL}/rest/synapse/latest/public/testPlan/{jira_no}/cycle/{cycle_id}/testRunsByCycleId",
                method='get',
                _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME), get_system_key(Constant.JIRA_PASSWORD))
            )

            if result != "":
                case_name_list = []
                logger.info('result结果：%s' % str(result.split(",")))
                for result_item in result.split(","):
                    logger.info('result_item：%s' % str(result_item))
                    case_list = jsonpath(json.loads(content.content),
                                               "$..[?(@.status == '%s')].summary" % result_item)
                    if case_list:
                        case_name_list += case_list
            else:
                case_name_list = jsonpath(json.loads(content.content), "$..summary")
        return case_name_list

    @classmethod
    def getDataByJql(self, jql, fields):
        content = list()
        try:
            content = APIDriver.http_request(
                url=f"{Constant.JIRA_URL}/rest/api/2/search",
                method='post',
                parametric_key='json',
                data={
                    "jql": jql,
                    "startAt": 0,
                    "maxResults": 1000,
                    "fields": fields
                },
                _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME), get_system_key(Constant.JIRA_PASSWORD))
            )
            content = json.loads(content.content)
            return content
        except Exception as e:
            logger.info(f'查询Jql异常：{jql}')
            return content

    @classmethod
    def saveCaseToTestPlan(self,testPlanIssueKey,jiraKey):
        content = list()
        try:
            content = APIDriver.http_request(
                url=f"{Constant.JIRA_URL}/rest/synapse/latest/public/testPlan/{testPlanIssueKey}/addMembers",
                method='post',
                parametric_key='json',
                data={
                    "testCaseKeys": jiraKey
                },
                _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME), get_system_key(Constant.JIRA_PASSWORD))
            )
            content = json.loads(content.content)
            return content
        except Exception as e:
            logger.info(f'添加测试用例到测试计划异常：{jql}')
            return content

    @classmethod
    def saveCaseToTestPlanByJql(self, testPlanIssueKey, jql):
        content = JiraPlatForm.getDataByJql(jql,["id", "key"])
        keys = jsonpath(content, "$.issues[*].key")
        logger.info(f'添加用例列表：'+str(keys))
        JiraPlatForm.saveCaseToTestPlan(testPlanIssueKey, keys)
        logger.info(f'提交到测试计划：' + str(testPlanIssueKey)+'成功')

    @classmethod
    def getCycleInfoByTestPlanIssueKey(self,testPlanIssueKey, cycle_id):
        try:
            logger.info(f"获取测试计划{testPlanIssueKey}周期编号{cycle_id}信息")
            content = APIDriver.http_request(
                url=f"{Constant.JIRA_URL}/rest/synapse/latest/public/testPlan/{testPlanIssueKey}/cycles",
                method='get',
                _auth=HTTPBasicAuth(get_system_key(Constant.JIRA_USERNAME), get_system_key(Constant.JIRA_PASSWORD)))
            cycleInfo = jsonpath(json.loads(content.content), f'$.[?(@.id=={cycle_id})]')[0]
            return cycleInfo
        except Exception as e:
            logger.info(f'获取测试计划：{testPlanIssueKey}中周期{cycle_id}信息异常信息:'+repr(e))
            return ""

if __name__ == '__main__':
    os.environ[Constant.JIRA_USERNAME] = '****'
    os.environ[Constant.JIRA_PASSWORD] = '***'
    os.environ[Constant.ISSUE_KEY] = 'DS21233-2178'
    JiraPlatForm.setJiraFlowStatus("2551")
