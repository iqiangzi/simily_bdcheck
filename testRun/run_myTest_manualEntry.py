#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
from testCase.models import myUnitChrome
from testCase.models.userVer.userVer import UserVer
from testCase.models.myTest.manualEntry import ManualEntry
from testResult.getResultImage import getResultImage


class RunManualEntry(myUnitChrome.UnitChrome):

    def login(self):
        userver=UserVer(self.driver)
        userver.userLogin("collegecheck","f")

    def atest_creatNewTask_succeed_run01(self):
        '''新建任务成功'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        confirm_name = me.getCreatTaskName()
        try:
            self.assertEqual(task_name,confirm_name,"新建任务失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_succeeful.jpg")
            sleep(3)

    def atest_selectExistingTasks_succeed_run02(self):
        '''选择已有任务成功'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        sleep(5)
        me.clickChooseBtn()
        me.clickDropDownBtn()
        old_name = me.clickOldTaskchoise()
        me.clickConfirmTaskBtn()
        confirm_name = me.getCreatTaskName()
        try:
            self.assertEqual(old_name,confirm_name,"选择已有任务失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"selectExistingTasks_succeed.jpg")
            sleep(3)

    def test_creatNewTask_sameName_run03(self):
        '''新建任务，任务名称重复'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        old_name = me.inputSameName()
        me.inputCreatTaskBox(old_name)
        me.clickConfirmTaskBtn()
        same_name_alert = me.getCreatTaskALert()
        try:
            self.assertEqual(same_name_alert,"您已创建过该任务；请重新创建或在已有任务中选择","名称重复未提示")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_sameName.jpg")
            sleep(3)


if __name__=="__main__":
    unittest.main()