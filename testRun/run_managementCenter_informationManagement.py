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
        '''进入信息管理，然后截图保存信息管理页面'''
        # 登录本科生系统
        login=UserVer(self.driver)
        login.userLogin("collegecheck","f")

        im=InformationManagement(self.driver)
        sleep(2)
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
        print("返回信息管理页面的记录总条数测试完成：")
        print(ab)
        sleep(2)

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"pageMsg.jpg")

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
        if firstTaskName=="ncy":
            print("用例通过")
        else:
            print("用例未通过！！！")
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
        if queryResult=="没有找到您要搜索的任务。":
            print("用例通过")
        else:
            print("用例未通过！！！")
        print("测试用例执行完成：输入数据库不存在的任务名称，进行检索。")

        # 对当前页面截图
        imagetest=getResultImage()
        imagetest.insert_image(self.driver,"query_taskNameNoExist.jpg")

if __name__=="__main__":
    unittest.main()
