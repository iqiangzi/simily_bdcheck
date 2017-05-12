#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    :
# @File    : run_informationManagement.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.managementCenter.informationManagement import InformationManagement
from testCase.models.managementCenter.basePageinformationMgmt import UserVer
from testCase.models.managementCenter.basePageinformationMgmt import BasePage
from time import sleep
from testResult.getResultImage import getResultImage

class RunInformationManagement(myUnitChrome.UnitChrome):
    def test_inInfoManageCenter_run(self):
        '''进入信息管理页面，然后截图保存信息管理页面'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        sleep(2)
        crumbs=im.inInfoManageCrumbs()
        self.assertEqual(crumbs,"信息管理")
        print("测试用例执行完成：进入管理中心-信息管理页面。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"inInfoManageCenter.jpg")

    def test_pageMsg_run(self):
        '''返回信息管理页面的记录总条数'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        sleep(2)
        ab=im.pageMsg()
        print("测试用例执行完成：返回信息管理页面的记录总条数")
        print("任务列表%s" %ab)
        sleep(2)

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pageMsg.jpg")

    def test_queryDirect_run(self):
        '''进入信息管理页面后，不输入查询条件，直接查询'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：不输入查询条件，直接查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryDirect.jpg")

    def test_queryAccountSelectLi1_run(self):
        '''选择检索条件 -- 账户 -- 下拉选择框 第一个元素'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.accountSelectLi1()
        sleep(2)

        im.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：选择检索条件 -- 账户 -- 下拉选择框 第一个元素,查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryAccountSelectLi1.jpg")

    def test_queryAccountSelectLi2_run(self):
        '''选择检索条件 -- 账户 -- 下拉选择框 第二个元素'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.accountSelectLi2()
        sleep(2)

        im.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：选择检索条件 -- 账户 -- 下拉选择框 第二个元素,查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryAccountSelectLi2.jpg")

    def test_query_taskName_run(self):
        '''输入数据库存在的任务名称，进行检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.inputTaskName("ncy")
        sleep(2)
        im.queryButtonClick()
        sleep(10)
        firstTaskName=im.queryFirstTaskName()
        self.assertEqual(firstTaskName,"ncy")
        print("测试用例执行完成：输入任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_taskName.jpg")

    def test_query_taskNameNoExist_run(self):
        '''输入数据库不存在的任务名称，进行检索，检索结果为空'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.inputTaskName("不存在")
        sleep(2)
        im.queryButtonClick()
        sleep(10)
        queryResult=im.queryIsNull()
        self.assertEqual(queryResult,"没有找到您要搜索的任务。")
        print("测试用例执行完成：输入数据库不存在的任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_taskNameNoExist.jpg")

    def test_query_partTaskName_run(self):
        '''输入部分任务名称，进行模糊检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.inputTaskName("批量")
        sleep(2)
        im.queryButtonClick()
        sleep(10)
        print("测试用例执行完成：输入任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_partTaskName.jpg")

    def test_query_completeTaskName_run(self):
        '''输入完整的任务名称，进行精确检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.inputTaskName("手工录入2017-05-04 09_04_25")
        sleep(2)
        im.queryButtonClick()
        sleep(10)
        firstTaskName=im.queryFirstTaskName()
        self.assertEqual(firstTaskName,"手工录入2017-05-04 09_04_25")
        print("测试用例执行完成：输入任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_completeTaskName.jpg")

    def test_query_longTaskName_run(self):
        '''输入特别长的任务名称，进行检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.inputTaskName("阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大")
        sleep(2)
        im.queryButtonClick()
        sleep(10)
        firstTaskName=im.queryFirstTaskName()
        self.assertEqual(firstTaskName,"阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大阿斯达所大")
        print("测试用例执行完成：输入特别长的任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_longTaskName.jpg")

    def test_queryTime1_run(self):
        '''选择创建开始时间和结束时间，进行检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.queryBeginTime(2016,5,11)
        sleep(5)
        im.queryEndTime(2017,12,25)
        sleep(5)
        im.queryButtonClick()
        print("测试用例执行完成：1111选择创建开始时间和结束时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTime1.jpg")

    def test_queryTimeOnlyBegin_run(self):
        '''只选择创建开始时间，不选择结束时间，进行检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.queryBeginTime(2016,5,11)
        sleep(2)
        im.queryButtonClick()
        print("测试用例执行完成：只选择创建开始时间，不选择结束时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTimeOnlyBegin.jpg")

    def test_queryTimeOnlyEnd_run(self):
        '''只选择创建结束时间，不选择开始时间，进行检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.queryEndTime(2017,12,25)
        sleep(2)
        im.queryButtonClick()
        print("测试用例执行完成：只选择创建结束时间，不选择开始时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTimeOnlyEnd.jpg")

    def test_queryUseAll_run(self):
        '''使用账户、任务名称、创建时间，进行多条件检索'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 选择账户（下拉列表第一个账户）
        im.accountSelectLi1()
        sleep(2)
        # 输入任务名称
        im.inputTaskName("ncy")
        sleep(2)
        # 选择创建时间
        im.queryBeginTime(2016,5,11)
        sleep(5)
        im.queryEndTime(2017,12,25)
        # 点击查询按钮
        im.queryButtonClick()
        sleep(2)
        firstAccount=im.queryFirstAccountName()
        self.assertEqual(firstAccount,"collegecheck")
        firstTaskName=im.queryFirstTaskName()
        self.assertEqual(firstTaskName,"ncy")
        print("测试用例执行完成：使用账户、任务名称、创建时间，进行多条件检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryUseAll.jpg")

    def test_inDetectResultPage_run(self):
        '''点击检测结果中第一条记录的任务名，进入任务检测结果页面。
        返回任务检测结果页面的面包屑：任务检测结果
        '''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 选择账户（下拉列表第一个账户）
        im.accountSelectLi1()
        sleep(2)
        # 输入任务名称
        im.inputTaskName("ncy")
        sleep(2)
        # 点击查询按钮
        im.queryButtonClick()
        sleep(2)
        # 点击任务名，进入检测结果页面
        result=im.inDetectResult()
        self.assertEqual(result,"任务检测结果")
        print("测试用例执行完成：点击检测结果中第一条记录的任务名，进入任务检测结果页面。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"inDetectResultPage.jpg")

    def test_pagingButtonSelect10_run(self):
        '''点击每页显示页数按钮，选择每页显示10条'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.pagingButtonSelect10()
        sleep(8)
        result=im.pagingSelect10Result()
        self.assertEqual(result,"10")
        print("测试用例执行完成：选择每页显示10条。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pagingButtonSelect10.jpg")

    def test_pagingButtonSelect20_run(self):
        '''点击每页显示页数按钮，选择每页显示20条'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.pagingButtonSelect20()
        sleep(8)
        result=im.pagingSelect20Result()
        self.assertEqual(result,"20")
        print("测试用例执行完成：选择每页显示20条。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pagingButtonSelect20.jpg")

    def test_pagingButtonSelect50_run(self):
        '''点击每页显示页数按钮，选择每页显示50条'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        im.pagingButtonSelect50()
        sleep(8)
        result=im.pagingSelect50Result()
        self.assertEqual(result,"50")
        print("测试用例执行完成：选择每页显示50条。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pagingButtonSelect50.jpg")

    def test_nextPage_run(self):
        '''位于首页时，点击下一页按钮'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 位于首页时，点击下一页按钮，进入第二页
        im.clickNextPage()
        sleep(2)
        # 点击下一页按钮，进入第三页
        im.clickNextPage()
        print("测试用例执行完成：位于首页时，点击下一页按钮。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"nextPage.jpg")

    def test_lastPage_run(self):
        '''位于首页时，点击尾页按钮'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 位于首页时，点击尾页按钮
        im.clickLastPage()
        sleep(2)
        print("测试用例执行完成：位于首页时，点击尾页按钮。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"lastPage.jpg")

    def test_previousPage_run(self):
        '''位于尾页时，点击上一页按钮'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 位于首页时，点击尾页按钮
        im.clickLastPage()
        sleep(2)
        # 位于尾页，点击上一页按钮
        im.clickPreviousPage()
        sleep(2)
        print("测试用例执行完成：位于尾页时，点击上一页按钮。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"previousPage.jpg")

    def test_firstPage_run(self):
        '''位于尾页时，点击首页按钮'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        # 位于首页时，点击尾页按钮
        im.clickLastPage()
        sleep(2)
        # 位于尾页，点击首页按钮
        im.clickFirstPage()
        sleep(2)
        print("测试用例执行完成：位于尾页时，点击首页按钮。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"firstPage.jpg")

if __name__=="__main__":
    unittest.main()
