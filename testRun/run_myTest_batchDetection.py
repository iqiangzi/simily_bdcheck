#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-09 10:01:51
# @Author  : Cys
# @Site    : 
# @File    : run_batchDetection.py
# @Software: PyCharm
import unittest
from testCase.models.userVer.userVer import UserVer
from time import sleep
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testResult.getResultImage import getResultImage
from testCase.models.myTest.batchDetection import BatchDetection

class RunBatchDetection(myUnitFirefox.UnitFirefox):

    def login(self):
        userver=UserVer(self.driver)
        userver.userLogin("collegecheck","f")

    def atest_creatNewTask_succeed_run01(self):
        '''新建任务成功'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_selectExistingTasks_succeed_run02(self):
        '''选择已有任务成功'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_creatNewTask_sameName_run03(self):
        '''新建任务，任务名称重复'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_creatNewTask_isnull_run04(self):
        '''新建任务，任务名称为空'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
        me.clickConfirmTaskBtn()
        try:
            self.assertTrue(me.isCreatAlertExist(),"-----没有错误提示-----")
            is_null_alert = me.getCreatTaskALert()
            self.assertEqual(is_null_alert,"任务名不能为空","-----任务名称为空未提示-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"creatNewTask_isnull.jpg")
            sleep(3)

    def atest_creatNewTask_overlong_run05(self):
        '''新建任务，任务名称过长'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_selectExistingTasks_notExist_run06(self):
        '''输入的已有任务名称不存在'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_selectExistingTasks_isnull_run07(self):
        '''不选择已有任务，直接点击'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_modifyCreatNewTask_succeed_run08(self):
        '''新建任务后，对任务名称进行修改'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        me.clickModifyBtn()
        modify_name = me.getDifferName()
        me.inputCreatTaskBox(modify_name)
        me.clickConfirmTaskBtn()
        confirm_name = me.getCreatTaskName()
        try:
            self.assertEqual(modify_name,confirm_name,"------修改任务名称失败--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_succeed.jpg")
            sleep(3)

    def atest_modifyCreatNewTask_samename_run09(self):
        '''新建任务后，修改任务名称名称重复的提示验证'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
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

    def atest_modifyCreatNewTask_isnull_run10(self):
        '''新建任务后，修改任务名称名为空的提示验证'''
        self.login()
        me = BatchDetection(self.driver)
        me.clickMyTes()
        me.clickBatchDetectBtn()
        task_name = me.getDifferName()
        me.inputCreatTaskBox(task_name)
        me.clickConfirmTaskBtn()
        me.clickModifyBtn()
        me.inputCreatTaskBox("")
        me.clickConfirmTaskBtn()
        same_name_alert = me.getCreatTaskALert()
        try:
            self.assertEqual(same_name_alert,"任务名不能为空","-----任务名称为空未提示-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"modifyCreatNewTask_isnull.jpg")
            sleep(3)

    def atest_repeatSelectExistingTasks_succeed_run11(self):
        '''选择已有任务,重新选择后，验证是否成功'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.clickBatchDetectBtn()
        sleep(2)
        bd.clickChooseBtn()
        bd.clickDropDownBtn()
        bd.clickOldTaskchoise()
        bd.clickConfirmTaskBtn()
        bd.clickRechoiseBtn()
        try:
            self.assertTrue(bd.isRechoiseClickable(),"-----重新选择不可点击------")
            bd.clickDropDownBtn()
            rechoise_name = bd.clickSecendOldTaskchoise()
            bd.clickConfirmTaskBtn()
            confirm_name = bd.getCreatTaskName()
            self.assertEqual(rechoise_name,confirm_name,"-----重新选择已有任务失败-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"repeatSelectExistingTasks_succeed.jpg")
            sleep(3)

    def atest_uploadfile_doc_detectsucceed_run12(self):
        '''上传doc文件，点击开始检测按钮'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_doc")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_doc_detectsucceed.jpg")
            sleep(3)

    def atest_uploadfile_docx_detectsucceed_run13(self):
        '''上传docx文件，点击开始检测按钮'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_docx_detectsucceed.jpg")
            sleep(3)

    def atest_uploadfile_pdf_detectsucceed_run14(self):
        '''上传pdf文件，点击开始检测按钮'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_pdf")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_pdf_detectsucceed.jpg")
            sleep(3)

    def atest_uploadfile_txt_detectsucceed_run15(self):
        '''上传txt文件，点击开始检测按钮'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_txt")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_txt_detectsucceed.jpg")
            sleep(3)

    def atest_uploadfile_rtf_detectsucceed_run16(self):
        '''上传rtf文件，点击开始检测按钮'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_rtf")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_rtf_detectsucceed.jpg")
            sleep(3)

    def atest_uploadfile_wrongtype_xls_run17(self):
        '''上传不符合上传文件类型的文件'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("excel_file_fail")
        try:
            is_alert = bd.is_alert_exist()
            self.assertTrue(is_alert,'-----上传不符合要求的文件类型时，未做提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_wrongtype_xls.jpg")
            sleep(3)

    def atest_uploadfile_oversize_run18(self):
        '''上传超过30M的文件'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("uploadfile_over30m")
        try:
            is_alert = bd.is_alert_exist()
            self.assertTrue(is_alert,'-----上传不符合要求的文件类型时，未做提示-----')
            sleep(5)
            alert_info = bd.getAlertInfo()
            self.assertIn("文件过大,上传失败！",alert_info,"-----文件超过30M，未做提示-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_oversize.jpg")
            sleep(3)

    def atest_uploadfile_name1_run19(self):
        '''上传名称为a+b+c格式的文件，点击开始检测按钮，验证是否提取成功'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        title = "相似性检测本科生论文+李硕+自定义名称"
        bd.uploadFile(title)
        try:
            extract_papername = bd.getExtractPaperName()
            papername = title.split("+")[0]
            self.assertEqual(extract_papername,papername,"-----论文名称提取失败-----")
            extract_authorname = bd.getExtractAuthorName()
            authorname = title.split("+")[1]
            self.assertEqual(extract_authorname,authorname,"-----作者名称提取失败-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_name1.jpg")
            sleep(3)

    def atest_uploadfile_name2_run20(self):
        '''上传名称为a+b格式的文件，点击开始检测按钮，验证是否提取成功'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        title = "相似性检测本科生论文+李硕"
        bd.uploadFile(title)
        try:
            extract_papername = bd.getExtractPaperName()
            papername = title.split("+")[0]
            self.assertEqual(extract_papername,papername,"-----论文名称提取失败-----")
            extract_authorname = bd.getExtractAuthorName()
            authorname = title.split("+")[1]
            self.assertEqual(extract_authorname,authorname,"-----作者名称提取失败-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_name2.jpg")
            sleep(3)

    def atest_detectpaper_wordnum_less5w_run21(self):
        '''检测少于5W字的论文，验证扣除篇数是否为1'''
        self.login()
        bd = BatchDetection(self.driver)
        remainnum_befdetect = int(bd.getRemainArticleNum())
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_less5w.docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
            remainnum_aftdetect = int(bd.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('1'),'-----扣除篇数错误，5w字以下应扣除1篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_less5w.jpg")
            sleep(3)

    def atest_detectpaper_wordnum_among5to10W_run22(self):
        '''检测大于5W字少于10W字的论文，验证扣除篇数是否为2'''
        self.login()
        bd = BatchDetection(self.driver)
        remainnum_befdetect = int(bd.getRemainArticleNum())
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_among5-10w.docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
            remainnum_aftdetect = int(bd.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('2'),'-----扣除篇数错误，5w-10w字应扣除2篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_among5to10W.jpg")
            sleep(3)

    def atest_detectpaper_wordnum_among10to15W_run23(self):
        '''检测大于10W字少于15W字的论文，验证扣除篇数是否为3'''
        self.login()
        bd = BatchDetection(self.driver)
        remainnum_befdetect = int(bd.getRemainArticleNum())
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_among10-15w.docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
            remainnum_aftdetect = int(bd.getRemainArticleNum())
            self.assertEqual(remainnum_befdetect-remainnum_aftdetect,int('3'),'-----扣除篇数错误，10w-15w字应扣除3篇-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"detectpaper_wordnum_among10to15W.jpg")
            sleep(3)

    def atest_uploadfile_size0kb_run24(self):
        '''上传文件大小为0kb的文件'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("uploadfile_blank.docx")
        try:
            is_alert = bd.is_alert_exist()
            self.assertTrue(is_alert,'-----上传0kb的文件时，未做相应提示-----')
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"uploadfile_size0kb.jpg")
            sleep(3)

    def atest_toCheckResult_run25(self):
        '''检测成功后跳转至查看检测结果页面'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        task_name = bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_docx.docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
            bd.clickCheckResultBtn()
            vertify_name = bd.getTaskName()
            self.assertEqual(vertify_name,task_name,"-----未跳转至检测结果页-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"toCheckResult.jpg")
            sleep(3)

    def test_toReCreat_run26(self):
        '''检测成功后跳转至创建任务页面'''
        self.login()
        bd = BatchDetection(self.driver)
        bd.clickMyTes()
        bd.batchDetectProcess()
        bd.clickAddPaperBtn()
        bd.uploadFile("detect_file_docx.docx")
        bd.clickBeginUploadBtn()
        try:
            is_upload_over = bd.isBeginDetectBtnExist()
            self.assertTrue(is_upload_over,'-----上传失败-----')
            bd.clickBeginDetectBtn()
            is_detect_over = bd.isCheckResultBtnExist()
            self.assertTrue(is_detect_over,"------检测未完成--------")
            succeed = bd.getDetectSimilarity()
            self.assertIn('%',succeed,"-------检测未成功--------")
            bd.clickReCreatBtn()
            confirm_exist = bd.isConfirmTaskBtnExist()
            self.assertTrue(confirm_exist,"-----未跳转至新建任务或选择已有任务页面-----")
        finally:
            imagetest = getResultImage()
            imagetest.insert_image(self.driver,"toCheckResult.jpg")
            sleep(3)


if __name__=="__main__":
    unittest.main()