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
from selenium.webdriver.support.ui import Select
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.userVer.userVer import UserVer
from testCase.models.myTest.taskList import TaskList
from testResult.getResultImage import getResultImage
from selenium.webdriver.common.by import By

class RunTaskList(myUnitChrome.UnitChrome):
    # 第一行复选框
    first_select_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]/input")
    task_search_loc = (By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[2]/input")
    # 篇名
    title_input_loc=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[1]/input[1]")
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
        flag=T.downVerify()
        if flag == True:
            # 修改文件名称
            T.renameFileName()
        # 勾选复选框，点击下载按钮
        T.downloadReport()
        # 点击弹出框的“确定按钮”
        self.driver.find_element_by_xpath(".//*[@id='confirmDownload']").click()
        time.sleep(3)
        flag1=T.downVerify()
        # 判断下载位置
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"report_down_success.jpg")

    def test_list1D_run(self):
        '''进入名称链接：下载报告-请选择检测信息'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 点击下载按钮
        self.driver.find_element_by_id("downLoadReport").click()
        # 点击弹出框的“确定按钮”
        self.driver.find_element_by_xpath(".//*[@id='confirmDownload']").click()
        time.sleep(3)
        msg=T.alert()
        # "请选择检测信息。"
        self.assertEqual(msg,"请选择检测信息。")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"report_down_fail.jpg")

    def test_list1E_run(self):
        '''进入名称链接：转移到其他任务-转移成功'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 输入篇名 点击搜索
        T.title_search("200字")
        time.sleep(1)
        # 勾选复选框
        self.driver.find_element_by_id("allchecked").click()
        # 转移到第一个任务
        T.transferTask()
        task=T.taskName()
        time.sleep(2)
        # 验证转移
        title=T.returnTask(task,"200字")
        self.assertIn("200字",title)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"transfer_task_success.jpg")

    def test_list1F_run(self):
        '''进入名称链接：转移到其他任务-请选择检测信息'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 点击下拉框，选择第一个
        T.transferTask()
        msg=T.alert()
        self.assertEqual(msg,"请选择检测信息。")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"transfer_task_fail.jpg")

    def test_list2A_run(self):
        '''进入名称链接：标记为-问题论文'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 勾选复选框
        self.driver.find_element(*self.first_select_loc).click()
        # 标记为问题论文
        T.markProblem()
        problem_num = T.paperNum()
        self.assertEqual(problem_num,"1")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"mark_paper_success.jpg")

    def test_list2B_run(self):
        '''进入名称链接：标记为-问题论文，请选择检测信息'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 标记为问题论文
        T.markProblem()
        time.sleep(1)
        msg=T.alert()
        self.assertEqual(msg,"请选择检测信息。")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"mark_paper_fail.jpg")
    def test_list2C_run(self):
        '''进入名称链接：取消标记为-问题论文'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 勾选复选框
        self.driver.find_element(*self.first_select_loc).click()
        # 标记为问题论文
        T.markProblem()
        time.sleep(2)
        # 勾选复选框
        self.driver.find_element(*self.first_select_loc).click()
        # 取消标记为问题论文
        T.concelMark()
        time.sleep(2)
        problem_num = T.paperNum()
        self.assertEqual(problem_num,"0")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"unmark_paper_success.jpg")
    def test_list2D_run(self):
        '''进入名称链接：取消标记为-问题论文,提示请选择'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 取消标记为问题论文
        T.concelMark()
        time.sleep(2)
        msg=T.alert()
        self.assertEqual(msg,"请选择检测信息。")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"unmark_paper_fail.jpg")

    def test_list3A_run(self):
        '''进入名称链接：篇名链接-上传论文可以点击下载到本地'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 输入篇名点击搜索
        T.title_search("医学期刊")
        new_title = T.paperNameLink()
        # print(new_title)
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 勾选复选框，点击下载按钮
        T.downloadReport()
        # 点击弹出框的“确定按钮”
        self.driver.find_element_by_xpath(".//*[@id='confirmDownload']").click()
        time.sleep(3)
        # 判断下载位置
        flag1=T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"click_name_link.jpg")

    def test_list3B_run(self):
        '''进入名称链接：作者链接-显示该作者的论文'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 输入篇名点击搜索
        T.title_search("医学")
        flag = T.authorLink()
        time.sleep(2)
        self.assertTrue(flag)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"click_author_link.jpg")

    def test_list3C_run(self):
        '''进入名称链接：检测时间排序'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("ncy")
        # 点击检测时间
        self.assertTrue(T.timeOrder())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"time_order_success.jpg")
    def test_list3D_run(self):
        '''进入名称链接：V1.0相似比排序'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        self.assertTrue(T.similarOrder())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"similarRadio_order_success.jpg")

    def test_list3E_run(self):
        '''进入名称链接：V2.0相似比排序'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        self.assertTrue(T.similarOrder1())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"similarRadio_order_successV2.0.jpg")

    def test_list4A_run(self):
        '''进入名称链接：下载 V2.0简明报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        # 1对应V2.0简明版
        report_type = T.downReport("1")
        str=report_type[:2]
        str_new="论文相似性检测报告"+"（V2.0"+str+"版）.pdf"
        title = T.loadReport1()
        new_title = title+str_new
        print(new_title)
        # 判断文件夹中是否存在
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 点击链接
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/a[1]").click()
        time.sleep(3)
        # 判断下载位置
        flag1=T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"concise_report_V2.0.jpg")

    def test_list4B_run(self):
        '''进入名称链接：下载 V2.0详细报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        # 2对应V2.0详细版
        report_type = T.downReport("2")
        str=report_type[:2]
        str_new="论文相似性检测报告"+"（V2.0"+str+"版）.pdf"
        title = T.loadReport1()
        new_title = title+str_new
        print(new_title)
        # 判断文件夹中是否存在
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 点击链接
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/a[3]").click()
        time.sleep(3)
        # 判断下载位置
        flag1=T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detail_report_V2.0.jpg")

    def test_list4C_run(self):
        '''进入名称链接：下载 V1.0简明报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        # 1对应简明报告
        report_type = T.downReport("1")
        str=report_type[:2]
        str_new="+论文相似性检测报告"+"（V1.0"+str+"版）.pdf"
        title = T.loadReport()
        new_title = title+str_new
        print(new_title)
        # 判断文件夹中是否存在
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 点击V1.0简明报告链接
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/a[2]").click()
        time.sleep(3)
        # 判断下载位置
        flag1 = T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"concise_report_V1.0.jpg")

    def test_list4D_run(self):
        '''进入名称链接：下载 V1.0详细报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        # 2对应详细报告
        report_type = T.downReport("2")
        str=report_type[:2]
        str_new="+论文相似性检测报告"+"（V1.0"+str+"版）.pdf"
        title = T.loadReport()
        new_title = title+str_new
        print(new_title)
        # 判断文件夹中是否存在
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 点击V1.0详细版链接
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/a[4]").click()
        time.sleep(3)
        # 判断下载位置
        flag1 = T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"detail_report_V1.0.jpg")

    def test_list4E_run(self):
        '''进入名称链接：下载 V1.0全文报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(2)
        # 3对应全文报告
        report_type = T.downReport("3")
        str=report_type[:2]
        str_new="+论文相似性检测报告"+"（V1.0"+str+"版）.pdf"
        title = T.loadReport()
        new_title = title+str_new
        print(new_title)
        # 判断文件夹中是否存在
        flag=T.downVerify1(new_title)
        if flag == True:
            # 修改文件名称
            T.renameFileName1(new_title)
        # 点击V1.0详细版链接
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/a[5]").click()
        time.sleep(3)
        # 判断下载位置
        flag1 = T.downVerify1(new_title)
        self.assertTrue(flag1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"full_report_V1.0.jpg")

    def test_list5A_run(self):
        '''进入名称链接：查看 V2.0在线报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(1)
        #self.driver.window_handles
        flag = T.onlineReport(1)
        self.assertTrue(flag)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"online_report_V2.0.jpg")

    def test_list5B_run(self):
        '''进入名称链接：查看 V！.0在线报告'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=TaskList(self.driver)
        # 进入名称链接
        T.taskNameLink("new_V")
        # 输入篇名点击搜索
        self.driver.find_element(*self.title_input_loc).send_keys("医学期刊简介")
        # 筛选检测成功的
        Select(self.driver.find_element_by_name("State")).select_by_visible_text("检测成功")
        self.driver.find_element(*self.task_search_loc).click()
        time.sleep(1)
        #self.driver.window_handles
        flag = T.onlineReport(2)
        self.assertFalse(flag)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"online_report_V1.0.jpg")




