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

    def atest_creatNewTask_sameName_run03(self):
        '''新建任务，任务名称重复'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        old_name = me.getSameName()
        me.inputCreatTaskBox(old_name)
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isCreatAlertExist(),"没有错误提示")
            same_name_alert = me.getCreatTaskALert()
            self.assertEqual(same_name_alert,"您已创建过该任务；请重新创建或在已有任务中选择","名称重复未提示")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_sameName.jpg")
            sleep(3)

    def atest_creatNewTask_isnull_run04(self):
            '''新建任务，任务名称为空'''
            self.login()
            me = ManualEntry(self.driver)
            me.clickMyTes()
            me.clickManualDetectButton()
            me.clickConfirmTaskBtn()
            try:
                self.assertTrue(me.isCreatAlertExist(),"没有错误提示")
                is_null_alert = me.getCreatTaskALert()
                self.assertEqual(is_null_alert,"任务名不能为空","任务名称为空未提示")
            finally:
                imagetest = getResultImage()
                imagetest.insert_image(self.driver,"creatNewTask_isnull.jpg")
                sleep(3)

    def atest_creatNewTask_overlong_run05(self):
            '''新建任务，任务名称过长'''
            self.login()
            me = ManualEntry(self.driver)
            me.clickMyTes()
            me.clickManualDetectButton()
            task_name = me.getOverLongName()
            me.inputCreatTaskBox(task_name)
            me.clickConfirmTaskBtn()
            try:
                self.assertTrue(me.isCreatAlertExist(),"没有错误提示")
                over_long_alert = me.getCreatTaskALert()
                self.assertEqual(over_long_alert,"任务名称最多xx字符","任务名称过长未提示")
            finally:
                imagetest = getResultImage()
                imagetest.insert_image(self.driver,"creatNewTask_overlong.jpg")
                sleep(3)

    def atest_selectExistingTasks_notExist_run06(self):
        '''输入的已有任务名称不存在'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        sleep(2)
        me.clickChooseBtn()
        me.inputOldTaskBox()
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isOldAlertExist,"没有错误提示")
            not_exist_alert = me.getOldTaskAlert()
            self.assertEqual(not_exist_alert,"没有您输入的已有任务","选择已有任务失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"selectExistingTasks_notExist.jpg")
            sleep(3)

    def atest_selectExistingTasks_isnull_run07(self):
        '''不选择已有任务，直接点击'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        sleep(2)
        me.clickChooseBtn()
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isOldAlertExist,"没有错误提示")
            is_null_alert = me.getOldTaskAlert()
            self.assertEqual(is_null_alert,"没有您输入的已有任务","选择已有任务失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"selectExistingTasks_isnull.jpg")
            sleep(3)

    def atest_modifyCreatNewTask_succeed_run08(self):
        '''新建任务后，对任务名称进行修改'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        me.clickModifyBtn()
        modify_name = task_name+'_2'
        me.inputCreatTaskBox(modify_name)
        me.clickConfirmTaskBtn()
        confirm_name = me.getCreatTaskName()
        try:
            self.assertEqual(modify_name,confirm_name,"修改任务名称失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_succeed.jpg")
            sleep(3)

    def atest_modifyCreatNewTask_samename_run09(self):
        '''新建任务后，修改任务名称名称重复的提示验证'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        me.clickModifyBtn()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        same_name_alert = me.getCreatTaskALert()
        try:
            self.assertEqual(same_name_alert,"您已创建过该任务；请重新创建或在已有任务中选择","任务名称重复未提示")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_samename.jpg")
            sleep(3)

    def atest_modifyCreatNewTask_isnull_run10(self):
        '''新建任务后，修改任务名称名为空的提示验证'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        me.clickModifyBtn()
        me.inputCreatTaskBox("")
        me.clickConfirmTaskBtn()
        same_name_alert = me.getCreatTaskALert()
        try:
            self.assertEqual(same_name_alert," 任务名不能为空","任务名称为空未提示")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_isnull.jpg")
            sleep(3)

    def atest_repeatSelectExistingTasks_succeed_run011(self):
        '''选择已有任务,重新选择后，验证是否成功'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        sleep(2)
        me.clickChooseBtn()
        me.clickDropDownBtn()
        me.clickOldTaskchoise()
        me.clickConfirmTaskBtn()
        me.clickRechoiseBtn()
        try:
            self.assertTrue(me.isRechoiseClickable())
            me.clickDropDownBtn()
            rechoise_name = me.clickSecendOldTaskchoise()
            me.clickConfirmTaskBtn()
            confirm_name = me.getCreatTaskName()
            self.assertEqual(rechoise_name,confirm_name,"重新选择已有任务失败")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"repeatSelectExistingTasks_succeed.jpg")
            sleep(3)

    def test_addContent_allField_succeed_run012(self):
        '''添加全部检测内容，点击开始检测'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        #me.manualEntryProcess()
        me.clickManualDetectButton()
        sleep(2)
        me.clickChooseBtn()
        me.clickDropDownBtn()
        me.clickOldTaskchoise()
        me.clickConfirmTaskBtn()
        sleep(10)


if __name__=="__main__":
    unittest.main()