#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_taskList.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.userVer.userVer import UserVer
from testCase.models.myTest.taskList import TaskList
from testResult.getResultImage import getResultImage

class RunTaskList(myUnitChrome.UnitChrome):
    def user_login_verify_run(self,username,password):
        '''
        用户登录用例运行
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        #print ("获取当前句柄",self.driver.current_window_handle)
        UserVer(self.driver).userLogin(username,password)
    def test_list0_run(self):
        ''' 任务列表：按照任务名称查询 '''
        self.user_login_verify_run("collegecheck","f")
        T=TaskList(self.driver)
        # T.list_search("批量检测")
        self.assertTrue(T.list_search("批量检测"))
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_name_search.jpg")
    def test_list1_run(self):
        '''任务列表：按照时间查询'''
        self.user_login_verify_run("collegecheck","f")
        T=TaskList(self.driver)
        #开始日期和结束日期都为当前年的4-1
        text=T.time_search("4","1","6","4","1","6")
        self.assertIn("04-01",text)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_time_search.jpg")
    def test_list2_run(self):
        '''任务列表：按照名称+时间查询'''
        self.user_login_verify_run("collegecheck","f")
        T=TaskList(self.driver)
        self.driver.find_element_by_id("taskNameInput").send_keys("批量检测")
        #开始日期和结束日期都为当前年的4-1
        text=T.time_search("4","1","6","4","1","6")
        self.assertIn("04-01",text)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_name&time_search.jpg")
    def test_list3_run(self):
        '''任务列表：表单测试-默认每页显示10条'''
        self.user_login_verify_run("collegecheck","f")
        list_num=len(self.driver.find_elements_by_xpath("html/body/div[4]/div[3]/table/tbody/tr/td[2]"))
        # list_n=str(list_num)
        self.assertEqual(list_num, 10)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_default_num.jpg")
    def test_list4_run(self):
        '''任务列表：表单测试-默认每页显示20条'''
        self.user_login_verify_run("collegecheck","f")
        T=TaskList(self.driver)
        list_n=T.pageChoose("2")
        self.assertEqual(list_n, 20)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_20_num.jpg")
    def test_list5_run(self):
        '''任务列表：表单测试-默认每页显示50条'''
        self.user_login_verify_run("collegecheck","f")
        T=TaskList(self.driver)
        list_n=T.pageChoose("3")
        self.assertEqual(list_n, 50)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_50_num.jpg")
    def test_list6_run(self):
        '''任务列表：表单测试-下一页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 点击 下一页 按钮
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/p/a[8]").click()
        self.assertEqual(T.pageNum(),"2")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_next_btn.jpg")
    def test_list7_run(self):
        '''任务列表：表单测试-末页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 点击 末页按钮
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/p/a[9]").click()
        # 现在尾页是163
        self.assertEqual(T.pageNum(),"163")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_last_btn.jpg")
    def test_list8_run(self):
        '''任务列表：表单测试-跳转页面'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        self.assertEqual(T.pageNum(),"3")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_pageSkip_btn.jpg")
    def test_list9_run(self):
        '''任务列表：表单测试-首页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        # 点击“首页”按钮
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/p/a[1]").click()
        self.assertEqual(T.pageNum(),"1")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_homePage_btn.jpg")
    def test_listA_run(self):
        '''任务列表：表单测试-上一页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        # 点击“上一页”按钮
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/p/a[2]").click()
        self.assertEqual(T.pageNum(),"2")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_upPage_btn.jpg")
    def test_listB_run(self):
        '''任务列表：检测状态-操作判断'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        self.assertTrue(T.statusOp())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_status_operation.jpg")
    def test_listC_run(self):
        '''任务列表：链接-名称链接'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        task_name,task_name_in=T.taskNameLink("ncy")
        self.assertEqual(task_name,task_name_in)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_name_link.jpg")
    def test_listD_run(self):
        '''任务列表：链接-操作链接'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        flag=T.operationLink("ncy")
        self.assertTrue(flag)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"task_op_link.jpg")
    def test_list1A_run(self):
        '''进入名称链接：查询条件--相似比,篇名和作者'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        flag = T.similarSearch(5,80,"Ch","医学")
        self.assertTrue(flag)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"search_STA_result.jpg")
    def test_list1B_run(self):
        '''进入名称链接：查询条件--检测时间，检测状态'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 选择时间 为今年的5月5日
        date=(T.timeStatusSearch(5,1,5,1,1,5,"检测成功"))
        self.assertIn("05-05",date)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"search_timeStatus_result.jpg")
    def test_list1C_run(self):
        '''进入名称链接：下载报告-下载成功'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 勾选复选框，点击下载按钮
        T.downloadReport()
        time.sleep(2)
        # 判断文件夹中是否为空
        T.renameFileName()
        # 点击弹出框的“确定按钮”
        self.driver.find_element_by_xpath(".//*[@id='confirmDownload']").click()
        time.sleep(3)
        # 判断下载位置
        self.assertTrue(T.downVerify())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"report_down_success.jpg")





    def test_operation_run(self):
        pass
    def test_taskNameLink_run(self):
        pass
    def test_taskLiskInfo_run(self):
        pass
    def test_paperquery_run(self):
        pass
    def test_downloadReport_run(self):
        pass
    def test_transferTask_run(self):
        pass
    def test_markForProblem_run(self):
        pass
    def test_cancelMarkPaper_run(self):
        pass
    def test_paperNameLink_run(self):
        pass
    def test_authorLink_run(self):
        pass
    def test_operation_run(self):
        pass
    def test_viewOnlineReports_run(self):
        pass
