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
from testCase.models.detectionResult.detectionResultPage import DetectionResultPage
from testCase.models.detectionResult.basePagedetectionResultPage import UserVer
from testCase.models.detectionResult.basePagedetectionResultPage import BasePage
# from testCase.pageObj.basePage import BasePage
from time import sleep
from testResult.getResultImage import getResultImage

class RunDetectionResultPage(myUnitChrome.UnitChrome):

    def loginBegin(self):
        '''登录系统'''
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")
        sleep(2)

    def test_inDetectResultPage_run(self):
        '''登录本科生，进入检测结果页面'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        pageTitle=dr.pageTitle()
        self.assertEqual(pageTitle,"论文检测详细信息")
        print("测试用例执行完成：登录本科生，进入检测结果页面。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"inDetectResultPage.jpg")

    def test_queryDirect_run(self):
        '''进入检测结果页面后，不输入查询条件，直接点击查询按钮'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.queryButtonClick()
        print("测试用例执行完成：进入检测结果页面后，不输入查询条件，直接点击查询按钮。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryDirect.jpg")

    def test_queryRatio_run(self):
        '''输入相似比进行检测'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputRatioBegin(10)
        dr.inputRatioEnd(70)
        dr.queryButtonClick()
        print("测试用例执行完成：输入相似比进行检测。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryRatio.jpg")

    def test_queryRatioOnlyBegin_run(self):
        '''只输入相似比-左边界值进行检测'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputRatioBegin(10)
        dr.queryButtonClick()
        print("测试用例执行完成：只输入相似比-左边界值进行检测。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryRatioOnlyBegin.jpg")

    def test_queryRatioOnlyEnd_run(self):
        '''只输入相似比-右边界值进行检测'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputRatioEnd(70)
        dr.queryButtonClick()
        print("测试用例执行完成：只输入相似比-右边界值进行检测。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryRatioOnlyEnd.jpg")

    def test_query_FileTitle_run(self):
        '''输入数据库存在的篇名，进行检索'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputFileTitle("南大算法")
        dr.queryButtonClick()
        title=dr.resultListFileTitle1()
        self.assertEqual(title,"南大算法")
        print("测试用例执行完成：输入数据库存在的篇名，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_FileTitle.jpg")

    def test_query_fileTitleNoExist_run(self):
        '''输入数据库不存在的篇名，进行检索，检索结果为空'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputFileTitle("不存在")
        dr.queryButtonClick()
        queryResult=dr.queryIsNull()
        print(queryResult)
        self.assertEqual(queryResult,"没有找到您要搜索的内容。")
        print("测试用例执行完成：输入数据库不存在的任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_fileTitleNoExist.jpg")

    def test_query_partFileTitle_run(self):
        '''输入部分篇名，进行模糊检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputFileTitle("相似")
        dr.queryButtonClick()
        print("测试用例执行完成：输入部分篇名，进行模糊检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_partFileTitle.jpg")

    def test_query_fullFiltTitle_run(self):
        '''输入完整的篇名，进行精确检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputFileTitle("相似性检测本科生论文")
        dr.queryButtonClick()
        title=dr.resultListFileTitle1()
        print(title)
        self.assertEqual(title,"相似性检测本科生论文")
        print("测试用例执行完成：输入完整的篇名，进行精确检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_fullFiltTitle.jpg")

    def test_query_longFiltTitle_run(self):
        '''输入特别长的任务名称，进行检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputFileTitle("1252025656556@白静@城市社区环境问题现状分析及对策建议@博士@赵导师")
        dr.queryButtonClick()
        title=dr.resultListFileTitle1()
        print(title)
        self.assertEqual(title,"1252025656556@白静@城市社区环境问题现状分析及对策建议@博士@赵导师")
        print("测试用例执行完成：输入特别长的任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_longFiltTitle.jpg")





    def test_query_Author_run(self):
        '''输入数据库存在的作者，进行检索'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputAuthor("李硕")
        dr.queryButtonClick()
        author=dr.resultListAuthor()
        self.assertEqual(author,"李硕")
        print("测试用例执行完成：输入数据库存在的作者，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_Author.jpg")

    def test_query_AuthorNoExist_run(self):
        '''输入数据库不存在的作者，进行检索，检索结果为空'''
        #登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputAuthor("不存在的作者")
        dr.queryButtonClick()
        queryResult=dr.queryIsNull()
        print(queryResult)
        self.assertEqual(queryResult,"没有找到您要搜索的内容。")
        print("测试用例执行完成：输入数据库不存在的作者，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_AuthorNoExist.jpg")

    def test_query_partAuthor_run(self):
        '''输入部分作者名，进行模糊检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputAuthor("李")
        dr.queryButtonClick()
        print("测试用例执行完成：输入部分作者名，进行模糊检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_partAuthor.jpg")

    def test_query_fullAuthor_run(self):
        '''输入完整的作者名，进行精确检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.inputAuthor("海鸣威")
        dr.queryButtonClick()
        author=dr.resultListAuthor()
        self.assertEqual(author,"海鸣威")
        print("测试用例执行完成：输入完整的作者名，进行精确检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_fullAuthor.jpg")

    def test_queryTime1_run(self):
        '''选择创建开始时间和结束时间，进行检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.queryBeginTime(2016,5,8)
        sleep(5)
        dr.queryEndTime(2017,12,29)
        sleep(5)
        dr.queryButtonClick()
        print("测试用例执行完成：选择创建开始时间和结束时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTime11.jpg")

    def test_queryTimeOnlyBegin_run(self):
        '''只选择创建开始时间，不选择结束时间，进行检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.queryBeginTime(2016,5,11)
        sleep(2)
        dr.queryButtonClick()
        print("测试用例执行完成：只选择创建开始时间，不选择结束时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTimeOnlyBegin1.jpg")

    def test_queryTimeOnlyEnd_run(self):
        '''只选择创建结束时间，不选择开始时间，进行检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.queryEndTime(2017,12,25)
        sleep(2)
        dr.queryButtonClick()
        print("测试用例执行完成：只选择创建结束时间，不选择开始时间，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTimeOnlyEnd1.jpg")

    def test_queryTaskNameSelectLi1_run(self):
        '''选择检索条件 -- 任务名称 -- 下拉选择框 第一个元素'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.taskNameSelectLi1()
        sleep(2)

        dr.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：选择检索条件 -- 任务名称 -- 下拉选择框 第一个元素,查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTaskNameSelectLi1.jpg")

    def test_queryTaskNameSelectLi2_run(self):
        '''选择检索条件 -- 任务名称 -- 下拉选择框 第二个元素'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.taskNameSelectLi2()
        sleep(2)

        dr.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：选择检索条件 -- 任务名称 -- 下拉选择框 第二个元素,查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryTaskNameSelectLi2.jpg")

    def test_clickIsTroubleFile_run(self):
        '''勾选问题论文，进行查询'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        dr.clickIsTroubleFile()
        sleep(2)

        dr.queryButtonClick()
        sleep(2)
        print("测试用例执行完成：勾选问题论文，进行查询。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"clickIsTroubleFile.jpg")

    def test_queryResultUseAll_run(self):
        '''使用所有的检测条件，进行多条件检索'''
        # 登录本科生系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        # 输入相似比
        dr.inputRatioBegin(10)
        dr.inputRatioEnd(70)
        # 输入篇名
        dr.inputFileTitle("相似性检测本科生论文")
        # 输入作者
        dr.inputAuthor("李硕")
        # 选择检测时间
        dr.queryBeginTime(2017,5,10)
        dr.queryEndTime(2017,5,17)
        # 选择任务名称
        dr.taskNameSelectLi1()
        sleep(2)

        dr.queryButtonClick()
        sleep(2)
        title=dr.resultListFileTitle1()
        print(title)
        self.assertEqual(title,"相似性检测本科生论文")
        author=dr.resultListAuthor()
        self.assertEqual(author,"李硕")
        print("测试用例执行完成：使用所有的检测条件，进行多条件检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"queryResultUseAll.jpg")

    def test_pageSum_run(self):
        '''刚进入检索结果页面后，返回记录总条数'''
        # 登录系统
        self.loginBegin()

        dr=DetectionResultPage(self.driver)
        pagesum=dr.pageSum()
        print("测试用例执行完成：刚进入检索结果页面后，返回记录总条数。")
        print("检测结果列表%s" %pagesum)

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pageSum.jpg")




