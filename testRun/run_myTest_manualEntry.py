#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from time import sleep
from testCase.models import myUnitFirefox
from testCase.models.userVer.userVer import UserVer
from testCase.models.myTest.manualEntry import ManualEntry
from testResult.getResultImage import getResultImage


class RunManualEntry(myUnitFirefox.UnitFirefox):

    def login(self):
        userver=UserVer(self.driver)
        userver.userLogin("collegecheck","f")

    def test_creatNewTask_succeed_run01(self):
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
            self.assertEqual(task_name,confirm_name,"-----新建任务失败-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_succeeful.jpg")
            sleep(3)

    def test_selectExistingTasks_succeed_run02(self):
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
            self.assertEqual(old_name,confirm_name,"-----选择已有任务失败-----")
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
        old_name = me.getSameName()
        me.inputCreatTaskBox(old_name)
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isCreatAlertExist(),"-----没有错误提示-----")
            same_name_alert = me.getCreatTaskALert()
            self.assertEqual(same_name_alert,"您已创建过该任务；请重新创建或在已有任务中选择","-----名称重复未提示-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_sameName.jpg")
            sleep(3)

    def test_creatNewTask_isnull_run04(self):
            '''新建任务，任务名称为空'''
            self.login()
            me = ManualEntry(self.driver)
            me.clickMyTes()
            me.clickManualDetectButton()
            me.clickConfirmTaskBtn()
            try:
                self.assertTrue(me.isCreatAlertExist(),"-----没有错误提示-----")
                is_null_alert = me.getCreatTaskALert()
                self.assertEqual(is_null_alert,"任务名不能为空","-------任务名称为空未提示--------")
            finally:
                imagetest = getResultImage()
                imagetest.insert_image(self.driver,"creatNewTask_isnull.jpg")
                sleep(3)

    def test_creatNewTask_overlong_run05(self):
            '''新建任务，任务名称过长'''
            self.login()
            me = ManualEntry(self.driver)
            me.clickMyTes()
            me.clickManualDetectButton()
            task_name = me.getOverLongName()
            me.inputCreatTaskBox(task_name)
            me.clickConfirmTaskBtn()
            try:
                self.assertTrue(me.isCreatAlertExist(),"-----没有错误提示-----")
                over_long_alert = me.getCreatTaskALert()
                self.assertEqual(over_long_alert,"任务名不能超过16位","-------任务名称过长未提示-------")
            finally:
                imagetest = getResultImage()
                imagetest.insert_image(self.driver,"creatNewTask_overlong.jpg")
                sleep(3)

    def test_selectExistingTasks_notExist_run06(self):
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
            self.assertTrue(me.isOldAlertExist,"-----没有错误提示-----")
            not_exist_alert = me.getOldTaskAlert()
            self.assertEqual(not_exist_alert,"没有您输入的已有任务","---------选择已有任务失败---------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"selectExistingTasks_notExist.jpg")
            sleep(3)

    def test_selectExistingTasks_isnull_run07(self):
        '''不选择已有任务，直接点击'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.clickManualDetectButton()
        sleep(2)
        me.clickChooseBtn()
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isOldAlertExist,"-----没有错误提示-----")
            is_null_alert = me.getOldTaskAlert()
            self.assertEqual(is_null_alert,"没有您输入的已有任务","-------选择已有任务失败-------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"selectExistingTasks_isnull.jpg")
            sleep(3)

    def test_modifyCreatNewTask_succeed_run08(self):
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
            self.assertEqual(modify_name,confirm_name,"------修改任务名称失败--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_succeed.jpg")
            sleep(3)

    def test_modifyCreatNewTask_samename_run09(self):
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
            self.assertEqual(same_name_alert,"您已创建过该任务；请重新创建或在已有任务中选择","-----任务名称重复未提示--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_samename.jpg")
            sleep(3)

    def test_modifyCreatNewTask_isnull_run10(self):
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
            self.assertEqual(same_name_alert," --------任务名不能为空","任务名称为空未提示-----------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_isnull.jpg")
            sleep(3)

    def test_repeatSelectExistingTasks_succeed_run11(self):
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
            self.assertEqual(rechoise_name,confirm_name,"--------重新选择已有任务失败----------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"repeatSelectExistingTasks_succeed.jpg")
            sleep(3)

    def test_addContent_allField_succeed_run12(self):
        '''添加全部检测内容，点击开始检测'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.inputAuthorCompany("文学出版社")
        me.inputMajority("文学专业")
        me.inputTutor("修导师")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-------论文未开始检测--------")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"------检测未完成--------")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_allField_succeed.jpg")
            sleep(3)

    def test_addContent_requiredField_succeed_run13(self):
        '''添加必填项检测内容，点击开始检测'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"test_addContent_requiredField_succeed.jpg")
            sleep(3)

    def test_addContent_paperName_isnull_run14(self):
        '''必填项篇名未填写，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'请输入篇名。','-----题名为空未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_paperName_isnull.jpg")
            sleep(3)

    def test_addContent_authorName_isnull_run15(self):
        '''必填项作者未填写，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'请输入作者。','-----作者为空未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_authorName_isnull.jpg")
            sleep(3)

    def test_addContent_content_isnull_run16(self):
        '''必填项录入内容未填写，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'请输入待检测内容。','-----录入内容为空未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_content_isnull.jpg")
            sleep(3)

    def test_addContent_content_less200_run17(self):
        '''必填项录入内容填写少于200字符，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file_less200.txt")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'待检测内容不得少于200字','-----录入内容少于200字未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_content_less200.jpg")
            sleep(3)

    def test_addContent_paperName_overlength_run18(self):
        '''篇名输入内容过长，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.readAndInputBigData("content_101.txt","paperName")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'篇名长度不能超过100字符','-----篇名长度过长未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_paperName_overlength.jpg")
            sleep(3)

    def test_addContent_authorName_overlength_run19(self):
        '''作者输入内容过长，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.readAndInputBigData("content_21.txt","authorName")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        papaerName_alert = me.verifyExistAlert()
        try:
            self.assertEqual(papaerName_alert,'作者长度不能超过20字符','-----作者长度过长未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_authorName_overlength.jpg")
            sleep(3)

    def test_addContent_authorCompany_overlength_run20(self):
        '''作者单位输入内容过长，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputBigData("content_101.txt","authorCompany")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        try:
            alert_exist = me.is_alert_exist()
            self.assertTrue(alert_exist,"-----作者单位长度过长未提示-----")
            papaerName_alert = me.verifyExistAlert()
            self.assertEqual(papaerName_alert,'作者单位长度不能超过100字符','-----作者单位长度过长未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_authorCompany_overlength.jpg")
            sleep(3)

    def test_addContent_majority_overlength_run21(self):
        '''专业输入内容过长，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputBigData("content_101.txt","majority")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        try:
            alert_exist = me.is_alert_exist()
            self.assertTrue(alert_exist,"-----专业长度过长未提示-----")
            papaerName_alert = me.verifyExistAlert()
            self.assertEqual(papaerName_alert,'专业长度不能超过100字符','-----专业长度过长未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_majority_overlength.jpg")
            sleep(3)

    def test_addContent_tutor_overlength_run22(self):
        '''导师输入内容过长，点击开始检测，检测提示信息'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputBigData("content_21.txt","tutor")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        try:
            alert_exist = me.is_alert_exist()
            self.assertTrue(alert_exist,"-----导师长度过长未提示-----")
            papaerName_alert = me.verifyExistAlert()
            self.assertEqual(papaerName_alert,'导师长度不能超过100字符','-----导师长度过长未提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"addContent_tutor_overlength.jpg")
            sleep(3)

    def test_detectpaper_wordnum_less5w_run23(self):
        '''检测少于5W字的论文，验证扣除篇数是否为1'''
        self.login()
        me = ManualEntry(self.driver)
        remainnum_befdetect = int(me.getRemainArticleNum())
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入_less5W")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file_less5w.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
            remainnum_aftdetect = int(me.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('1'),'-----扣除篇数错误，5w字以下应扣除1篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_less5w.jpg")
            sleep(3)

    def test_detectpaper_wordnum_among5to10W_run24(self):
        '''检测大于5W字少于10W字的论文，验证扣除篇数是否为2'''
        self.login()
        me = ManualEntry(self.driver)
        remainnum_befdetect = int(me.getRemainArticleNum())
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入_5-10W")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file_among5-10w.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
            remainnum_aftdetect = int(me.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('2'),'-----扣除篇数错误，5w-10w字应扣除2篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_among5to10W.jpg")
            sleep(3)

    def test_detectpaper_wordnum_among10to15W_run24(self):
        '''检测大于10W字少于15W字的论文，验证扣除篇数是否为3'''
        self.login()
        me = ManualEntry(self.driver)
        remainnum_befdetect = int(me.getRemainArticleNum())
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入_10-15W")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file_among10-15w.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
            remainnum_aftdetect = int(me.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('3'),'-----扣除篇数错误，10w-15w字应扣除3篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_among10to15W.jpg")
            sleep(3)

    def test_toCheckResult_run25(self):
        '''检测成功后跳转至查看检测结果页面'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        task_name = me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
            me.clickCheckResultBtn()
            vertify_name = me.getTaskName()
            self.assertEqual(vertify_name,task_name,"-----未跳转至检测结果页-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"toCheckResult.jpg")
            sleep(3)

    def test_toReCreat_run26(self):
        '''检测成功后跳转至创建任务页面'''
        self.login()
        me = ManualEntry(self.driver)
        me.clickMyTes()
        me.manualEntryProcess()
        me.inputPaperName("手工录入")
        me.inputAuthorName("海鸣威")
        me.readAndInputContent("detect_file.txt")
        me.clickBeginDetectBtn()
        state = me.getDetectState()
        try:
            self.assertEqual(state,"开始检测","-----论文未开始检测-----")
            finish = me.isCheckResultBtnExist()
            self.assertTrue(finish,"-----论文检测未完成-----")
            succeed = me.getDetectSimilarity()
            self.assertIn('%',succeed,"-----论文检测未成功-----")
            me.clickReCreatBtn()
            confirm_exist = me.isConfirmTaskBtnExist()
            self.assertTrue(confirm_exist,"-----未跳转至新建任务或选择已有任务页面-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"toReCreat.jpg")
            sleep(3)


if __name__=="__main__":
    unittest.main()