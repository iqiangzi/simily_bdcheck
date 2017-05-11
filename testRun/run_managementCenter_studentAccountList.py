#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    :
# @File    : run_studentAccount.py
# @Software: PyCharm
from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

from testCase.models.managementCenter.basePagestudentAccount import UserVer
from testCase.models.managementCenter.studentAccountList import StuAccountList
from testResult.getResultImage import getResultImage
from selenium.webdriver.common.by import By

class RunStudentAccount(myUnitChrome.UnitChrome):
    # 子账户
    fist_sub_account = (By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[2]/a")
    def user_login_verify_run(self,username,password):
        '''
        用户登录用例运行
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        UserVer(self.driver).userLogin(username,password)
    def test_search_run(self):
        '''查询：日期 查询'''
        self.user_login_verify_run("collegecheck","f")
        S=StuAccountList(self.driver)
        # 选的时间范围 04-01 04-28
        S.timeSearch("4","1","6","1","5","5")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        # 第一行的时间
        first_line = S.firstTime()
        if first_line >= "2017-04-01" and first_line <= "2017-04-28":
            flag = True
            self.assertTrue(flag)
            #获取页面截图
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"stuAccount_timeSearch_success.jpg")
    def test_search1_run(self):
        '''查询：批次名称 查询'''
        self.user_login_verify_run("collegecheck","f")
        S=StuAccountList(self.driver)
        S.batchSearch("2017")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        # 返回批次名称
        batch = S.firstBatch()
        self.assertIn("2017", batch)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccount_batchSearch_success.jpg")
    def test_search2_run(self):
        '''查询：时间和批次名称 查询'''
        self.user_login_verify_run("collegecheck","f")
        S=StuAccountList(self.driver)
        # 选的时间范围 04-01 04-28
        S.timeSearch("4","1","6","1","5","5")
        S.batchSearch("2017")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        # 返回批次名称
        batch = S.firstBatch()
        self.assertIn("2017", batch)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccount_t&batchSearch_success.jpg")

    def test_export_run(self):
        '''导出：导出信息表'''
        self.user_login_verify_run("collegecheck","f")
        S=StuAccountList(self.driver)
        now_title="大学生论文检测-学生账户批次信息表.xls"
        flag = S.downVerify1(now_title)
        if flag == True:
            S.renameFileName1(now_title,".xls")
        # 点击导出按钮
        self.driver.find_element_by_xpath(".//*[@id='exportForm']/button").click()
        time.sleep(3)
        flag1 = S.downVerify1(now_title)
        self.assertTrue(flag1)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccount_export_success.jpg")


    def test_paging_run(self):
        '''任务列表：表单测试-默认每页显示10条'''
        self.user_login_verify_run("collegecheck","f")
        list_num=len(self.driver.find_elements_by_xpath(".//*[@id='container']/table/tbody/tr/td[3]"))
        # list_n=str(list_num)
        self.assertEqual(list_num, 10)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_default_num.jpg")
    def test_paging1_run(self):
        '''任务列表：表单测试-默认每页显示20条'''
        self.user_login_verify_run("collegecheck","f")
        T=StuAccountList(self.driver)
        list_n=T.pageChoose("2")
        self.assertEqual(list_n, 20)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_20_num.jpg")
    def test_paging2_run(self):
        '''任务列表：表单测试-默认每页显示50条'''
        self.user_login_verify_run("collegecheck","f")
        T=StuAccountList(self.driver)
        list_n=T.pageChoose("3")
        self.assertEqual(list_n, 50)
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_50_num.jpg")
    def test_paging3_run(self):
        '''任务列表：表单测试-下一页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=StuAccountList(self.driver)
        # 点击 下一页 按钮
        self.driver.find_element_by_xpath(".//*[@id='container']/div/form/p/a[8]").click()
        self.assertEqual(T.pageNum(), "2")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_next_btn.jpg")
    def test_paging4_run(self):
        '''任务列表：表单测试-末页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=StuAccountList(self.driver)
        # 点击 末页按钮
        self.driver.find_element_by_xpath(".//*[@id='container']/div/form/p/a[9]").click()
        # 现在尾页是7
        self.assertEqual(T.pageNum(),"7")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_last_btn.jpg")
    def test_paging5_run(self):
        '''任务列表：表单测试-跳转页面'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=StuAccountList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        self.assertEqual(T.pageNum(),"3")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tasklist_pageSkip_btn.jpg")
    def test_paging6_run(self):
        '''任务列表：表单测试-首页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=StuAccountList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        # 点击“首页”按钮
        self.driver.find_element_by_xpath(".//*[@id='container']/div/form/p/a[1]").click()
        self.assertEqual(T.pageNum(),"1")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_homePage_btn.jpg")
    def test_paging7_run(self):
        '''任务列表：表单测试-上一页按钮'''
        self.user_login_verify_run("collegecheck","f")
        time.sleep(1)
        T=StuAccountList(self.driver)
        # 跳转到第3页
        T.pageSkip(3)
        # 点击“上一页”按钮
        self.driver.find_element_by_xpath(".//*[@id='container']/div/form/p/a[2]").click()
        self.assertEqual(T.pageNum(),"2")
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_upPage_btn.jpg")

    def test_accountNumLink_run(self):
        '''任务列表：数量链接'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        batch=S.firstBatch()
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        time.sleep(1)
        detail_batch=self.driver.find_element_by_xpath(".//*[@id='select-box']/input[1]").get_attribute('value')
        # print(detail_batch)
        self.assertEqual(batch,detail_batch)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuList_numLink_btn.jpg")

    def test_accountNumLink1_run(self):
        '''信息列表：数量链接进入 导出列表'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # batch=S.firstBatch()
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        now_title="大学生论文检测-lytest123账户信息表.xls"
        flag = S.downVerify1(now_title)
        if flag == True:
            S.renameFileName1(now_title,".xls")
        # 单击导出按钮
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/button").click()
        time.sleep(3)
        flag1 = S.downVerify1(now_title)
        self.assertTrue(flag1)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccount_export1_success.jpg")

    def test_accountNumLink2_run(self):
        '''信息列表：数量链接进入 根据批次和学生账号查询'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 批次和学生账户查询
        S.batchAccount("3", "collegeuser.201219110210")
        # 点击查询按钮
        S.searchBtn()
        batch,account=S.batchMsg()
        if batch == "lytest123" and account == "collegeuser.201219110210":
            flag = True
            self.assertTrue(flag)
            #获取页面截图
            imagetest = getResultImage()
            imagetest.insert_image(self.driver, "stuAccount_search1_success.jpg")

    def test_accountNumLink3_run(self):
        '''信息列表：数量链接进入 根据相似比和检测次数查询'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 批次和学生账户查询
        S.similarTest("0","65","0","2")
        # 点击查询按钮
        S.searchBtn()
        # 比较相似比和检测次数
        flag = S.similarMsg("0","65","0","2")
        self.assertTrue(flag)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "stuAccount_search2_success.jpg")

    def test_accountNumLink4_run(self):
        '''信息列表：学生账号详情 -进入个人详情'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 点击第一个账号链接
        flag = S.accountLink()
        self.assertTrue(flag)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "personalAccount_in_success.jpg")

    def test_accountNumLink5_run(self):
        '''信息列表：进入个人详情-检测情况为0'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        self.assertEqual(S.personalTest(),"该学生没有检测。")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "perAccount_testNum0_success.jpg")

    def test_accountNumLink6_run(self):
        '''信息列表：进入个人详情-检测情况为0'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        S.batchAccount("3","collegeuser.201219110210")
        # 点击查询按钮
        S.searchBtn()
        self.assertFalse(S.personalTest())
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "perAccount_testNum0_fail.jpg")

    def test_accountNumLink7_run(self):
        '''信息列表：学生详情-更改有效期'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 更改第一行的 有效期
        S.optionBtn("更改有效期","1")
        # 选择6月1日
        time_display = S.optionTime("2","1","4")
        self.assertEqual(time_display,"2017.06.01")
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "stu_alterTime_success.jpg")

    def test_accountNumLink8_run(self):
        '''信息列表：学生详情-增加篇数'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        old_article = int(self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[10]").text)
        # 增加第一行的篇数
        S.optionBtn("增加篇数","1")
        # 增加2篇
        S.addArticle(2)
        now_article = int(self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[10]").text)
        self.assertEqual(old_article+2,now_article)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "stu_addArticle_success.jpg")

    def test_accountNumLink9_run(self):
        '''信息列表：学生详情-转移批次'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 返回第一行的子账户
        sub_account = self.driver.find_element(*self.fist_sub_account).text
        # 转移批次
        S.optionBtn("转移批次","1")
        # 2对应批次lytest111
        i = 2
        S.transferBatch(i)
        time.sleep(2)
        # 进入对应批次查询
        S.batchAccount(i, sub_account)
        # 点击查询按钮
        S.searchBtn()
        # 返回第一行的子账户
        sub_account1 = self.driver.find_element(*self.fist_sub_account).text
        self.assertEqual(sub_account,sub_account1)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "stu_transferBatch_success.jpg")

    def test_accountNumLinkA_run(self):
        '''信息列表：进入个人详情-题名链接-下载'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 根据相似比和检测次数进行查询
        # 批次和学生账户查询
        S.similarTest("60","65","2","5")
        # 点击查询按钮
        S.searchBtn()
        # 点击名称链接
        self.driver.find_element(*self.fist_sub_account).click()
        time.sleep(1)
        # 点击第一行名称链接 2对应第一行
        row = 2
        file_name = S.personalPaper(row)
        new_title= "%s.pdf" % file_name
        # print(new_title)
        flag = S.downVerify1(new_title)
        if flag == True:
            S.renameFileName1(new_title,".pdf")
        # 点击名称链接进行下载论文
        self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[%s]/td[1]/a" % row).click()
        time.sleep(3)
        flag1 = S.downVerify1(new_title)
        self.assertTrue(flag1)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "personal_download_success.jpg")

    def test_accountNumLinkB_run(self):
        '''信息列表：进入个人详情-下载V2.0详细报告'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 根据相似比和检测次数进行查询
        # 批次和学生账户查询
        S.similarTest("60","65","2","5")
        # 点击查询按钮
        S.searchBtn()
        # 点击名称链接
        self.driver.find_element(*self.fist_sub_account).click()
        time.sleep(1)
        # 点击第一行名称链接 2对应第一行
        row = 2
        file_name = S.personalPaper(row)
        verion = S.personalDown(1)
        new_title = "《" + file_name + "》 论文相似性检测报告（"+"V2.0"+verion+"版）.pdf"
        print(new_title)
        flag = S.downVerify1(new_title)
        if flag == True:
            S.renameFileName1(new_title,".pdf")
        # 点击版本链接 下载详细报告V2.0
        S.versionLink(6,1)
        time.sleep(3)
        flag1 = S.downVerify1(new_title)
        self.assertTrue(flag1)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "personal_detailV2.0_success.jpg")

    def test_accountNumLinkC_run(self):
        '''信息列表：进入个人详情-下载V1.0详细报告'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 根据相似比和检测次数进行查询
        # 批次和学生账户查询
        S.similarTest("60","65","2","5")
        # 点击查询按钮
        S.searchBtn()
        # 点击名称链接
        self.driver.find_element(*self.fist_sub_account).click()
        time.sleep(1)
        # 点击第一行名称链接 2对应第一行
        row = 2
        file_name = S.personalPaper(row)
        verion = S.personalDown(1)
        new_title = "《" + file_name + "》 论文相似性检测报告（"+"V1.0"+verion+"版）.pdf"
        print(new_title)
        flag = S.downVerify1(new_title)
        if flag == True:
            S.renameFileName1(new_title,".pdf")
        # 点击版本链接 下载详细报告V1.0
        S.versionLink(6,2)
        time.sleep(3)
        flag1 = S.downVerify1(new_title)
        self.assertTrue(flag1)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "personal_detailV1.0_success.jpg")

    def test_accountNumLinkD_run(self):
        '''信息列表：进入个人详情-下载V1.0全文报告'''
        self.user_login_verify_run("collegeuser","f")
        time.sleep(1)
        S=StuAccountList(self.driver)
        S.batchSearch("lytest123")
        # 点击搜索按钮
        self.driver.find_element_by_id("searchBtn").click()
        time.sleep(1)
        # 点击数量链接
        self.driver.find_element_by_xpath(".//*[@id='container']/table/tbody/tr[2]/td[4]/a/b").click()
        # 根据相似比和检测次数进行查询
        # 批次和学生账户查询
        S.similarTest("60","65","2","5")
        # 点击查询按钮
        S.searchBtn()
        # 点击名称链接
        self.driver.find_element(*self.fist_sub_account).click()
        time.sleep(1)
        # 点击第一行名称链接 2对应第一行
        row = 2
        file_name = S.personalPaper(row)
        # 全文报告对应2
        verion = S.personalDown(2)
        new_title = "《" + file_name + "》 论文相似性检测报告（"+"V1.0"+verion+"报告）.pdf"
        print(new_title)
        flag = S.downVerify1(new_title)
        if flag == True:
            S.renameFileName1(new_title, ".pdf")
        # 点击版本链接 下载全文报告V1.0
        S.versionLink(6,3)
        time.sleep(3)
        flag1 = S.downVerify1(new_title)
        self.assertTrue(flag1)
        # 获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver, "personal_fullV1.0_success.jpg")

if __name__=="__main__":
    unittest.main()