#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : batchDetection.py
# @Software: PyCharm
from util.commonUtils.upLoad import UpLoad
from selenium.webdriver.common.by import By
from testCase.pageObj.basePage import BasePage
from time import sleep,strftime

class BatchDetection(BasePage):

    #新建和选择已有任务相关********************************************************************************

    myTestTab = (By.CSS_SELECTOR,'#myCheck>a')  #顶部导航栏-我的检测
    batchDetectButton = (By.CSS_SELECTOR,'.colleupbtn')   #批量检测按钮
    creatTaskBox = (By.CSS_SELECTOR,'#taskNameNew')   #创建新任务输入框
    chooseBtn = (By.CSS_SELECTOR,'#taskRib2')   #选择已有任务选择框
    chooseBtn1 = (By.CSS_SELECTOR,'#taskRib1')   #选择新建任务选择框
    oldTaskBox = (By.CSS_SELECTOR,'#taskNameOld')    #选择已有任务输入模式
    oldTaskchoise1 = (By.CSS_SELECTOR,'#taskNameOldDown')  #下拉选项按钮
    oldTaskchoise = (By.CSS_SELECTOR,'body>.ac_results>ul>li:nth-child(1)')  #下拉选项的首个任务
    oldTaskchoise2 = (By.CSS_SELECTOR,'body>.ac_results>ul>li:nth-child(2)')  #下拉选项的第二个任务
    oldTaskAlert = (By.CSS_SELECTOR,'#oldTaskAlert>.colRed') #输入已有任务的错误提示
    creatTaskALert = (By.CSS_SELECTOR,'#creatTaskAlert>.colRed') #创建新任务错误提示
    confirmTaskBtn = (By.CSS_SELECTOR,'#confirmTaskNameBtn') #确认任务名称按钮
    creatTaskName = (By.CSS_SELECTOR,'.collereTask>.taskName') #新建任务名称确认
    modifyTaskName = (By.CSS_SELECTOR,'.collereTask>#reNewTaskName') #修改任务名称按钮
    rechoiseBtn = (By.CSS_SELECTOR,'.collereTask>#reChoseOldTask') #重新选择任务按钮

    #批量检测内容相关****************************************************************************************

    addPaperBtn = (By.CSS_SELECTOR,'#addPaper>div:nth-child(2)') #添加论文按钮
    beginUploadBtn = (By.CSS_SELECTOR,'#beginUpload') #开始上传按钮
    beginDetectBtn = (By.CSS_SELECTOR,'#beginCheck') #开始检测按钮
    checkResultBtn = (By.CSS_SELECTOR,'#checkResult') #查看检测结果按钮
    reCreatBtn = (By.CSS_SELECTOR,'#reCreat') #继续创建新任务按钮
    detectSimilarity = (By.CSS_SELECTOR,'#uploadPaperList>table>tbody>tr:nth-child(2)>.similarity') #检测页面的相似比
    extractPaperName = (By.CSS_SELECTOR,'#uploadPaperList>table>tbody>tr:nth-child(2)>.paperName') #提取的论文名称
    extractAuthorName = (By.CSS_SELECTOR,'#uploadPaperList>table>tbody>tr:nth-child(2)>.authorName') #提取的作者名称
    checkResultTaskName = (By.CSS_SELECTOR,'.paperLguide>b') #查看检测结果页面的任务名称

    #检测结果页面确认***********************************************************************************************

    accountManageTab = (By.CSS_SELECTOR,'#manageCenterList>li:nth-child(1)>a') #账号管理导航按钮
    manageCenter= (By.CSS_SELECTOR,'#manageCenter>a') #管理中心按钮
    remainArticleNum = (By.CSS_SELECTOR,'#surplusCheckCount') #剩余篇数

    '''************************************新建任务和选择已有任务相关操作***************************************'''
   #点击我的检测
    def clickMyTes(self):
        self.find_element(*self.myTestTab).click()
        sleep(2)
    #点击手工录入按钮
    def clickBatchDetectBtn(self):
        self.find_element(*self.batchDetectButton).click()
        sleep(3)
    #输入新建任务名称
    def inputCreatTaskBox(self,task_name):
        self.find_element(*self.creatTaskBox).clear()
        self.find_element(*self.creatTaskBox).send_keys(task_name)
        sleep(2)
    #获取新建任务时的不重名称
    def getDifferName(self):
        tag=strftime("%Y%m%d%H%M%S")
        name="批量%s"%(tag)
        return name
    #点击确认任务名称按钮
    def clickConfirmTaskBtn(self):
        self.find_element(*self.confirmTaskBtn).click()
        sleep(2)
    #获取新建任务后的任务名称
    def getCreatTaskName(self):
        return self.find_element(*self.creatTaskName).text
    #点击切换到选择已有任务按钮
    def clickChooseBtn(self):
        self.find_element(*self.chooseBtn).click()
        sleep(2)
    #点击下拉按钮
    def clickDropDownBtn(self):
        self.find_element(*self.oldTaskchoise1).click()
        sleep(2)
    #选择已有任务
    def clickOldTaskchoise(self):
        old_name = self.find_element(*self.oldTaskchoise).text
        sleep(2)
        self.find_element(*self.oldTaskchoise).click()
        sleep(2)
        return old_name
    #选择已有任务，第二个
    def clickSecendOldTaskchoise(self):
        old_name = self.find_element(*self.oldTaskchoise2).text
        sleep(2)
        self.find_element(*self.oldTaskchoise2).click()
        sleep(2)
        return old_name
    #点击新建任务选择框
    def clickChooseBtn1(self):
        self.find_element(*self.chooseBtn1).click()
        sleep(2)
    #输入已存在的任务名称
    def getSameName(self):
        #切换至已有任务
        self.clickChooseBtn()
        #获取已有任务名称
        self.clickDropDownBtn()
        old_name = self.clickOldTaskchoise()
        #切换至新建任务
        self.clickChooseBtn1()
        return old_name
    #获取新建任务时的错误提示
    def getCreatTaskALert(self):
        return  self.find_element(*self.creatTaskALert).text
    #得到字符超长的任务名
    def getOverLongName(self):
        long_name = "长度的测试"
        long_name*=4
        #print(len(long_name))
        return long_name
    #判断新建任务时的错误提示是否存在，如果存在返回flag=true，否则返回false
    def isCreatAlertExist(self):
        flag = super(BatchDetection, self).is_element_visible(self.creatTaskALert)
        print('flag is:%s'%flag)
        return flag
    #获取选择已有任务时的错误提示
    def getOldTaskAlert(self):
        return  self.find_element(*self.oldTaskAlert).text
    #判断选择已有任务时的错误提示是否存在，如果存在返回flag=true，否则返回false
    def isOldAlertExist(self):
        flag = super(BatchDetection, self).is_element_visible(self.oldTaskAlert)
        return flag
    #输入已有任务名称
    def inputOldTaskBox(self):
        self.find_element(*self.oldTaskBox).clear()
        self.find_element(*self.oldTaskBox).send_keys("不存在的任务名称")
        sleep(2)
    #新建任务点击修改
    def clickModifyBtn(self):
        self.find_element(*self.modifyTaskName).click()
        sleep(2)
    #选择已有任务点击重新选择
    def clickRechoiseBtn(self):
        self.find_element(*self.rechoiseBtn).click()
        sleep(2)
    #判断页面中某元素是否可点击
    def isRechoiseClickable(self):
        flag = super(BatchDetection,self).is_element_clickable(self.oldTaskchoise1)
        #print(flag)
        return flag

    '''**********************************************批量上传相关操作*************************************************'''

    #批量检测选择任务过程
    def batchDetectProcess(self):
        self.find_element(*self.batchDetectButton).click()
        sleep(3)
        self.find_element(*self.chooseBtn).click()
        sleep(2)
        self.find_element(*self.oldTaskchoise1).click()
        sleep(2)
        name = self.clickOldTaskchoise()
        sleep(2)
        self.find_element(*self.confirmTaskBtn).click()
        sleep(2)
        return  name
    #点击添加论文按钮
    def clickAddPaperBtn(self):
        self.find_element(*self.addPaperBtn).click()
        sleep(2)
    #判断autoit上传文件是否成功，开始上传按钮是否出现
    def isBeginUploadBtnExist(self,waittime):
        flag = True
        #star = time()
        wait_time = 0
        while flag:
            isVisiable = super(BatchDetection, self).is_element_visible(self.beginUploadBtn)
            #end = time()
            #wait_time = int(end-star)
            if isVisiable == True:
                print("-----autoit上传成功！------")
                return isVisiable
            elif isVisiable == False:
                print("等待autoit上传: %ss"%wait_time)
                if wait_time >= waittime:
                    print("-----等待autoit上传超时！-----")
                    return isVisiable
                else:
                    wait_time+=1
                    sleep(1)
                    continue
    #上传文件操作
    def uploadFile(self,filename):
        ul = UpLoad()
        filepath = ul.getFilePath("detectPaper",filename)
        ul.uploadFile_para("chrome",filepath)
        self.isBeginUploadBtnExist(6)
    #点击开始上传
    def clickBeginUploadBtn(self):
        self.find_element(*self.beginUploadBtn).click()
        sleep(2)
    #判断上传文件是否成功，开始检测按钮是否出现
    def isBeginDetectBtnExist(self):
        flag = True
        #star = time()
        wait_time = 0
        while flag:
            isVisiable = super(BatchDetection, self).is_element_visible(self.beginDetectBtn)
            #end = time()
            #wait_time = int(end-star)
            if isVisiable == True:
                print("-----上传成功！------")
                return isVisiable
            elif isVisiable == False:
                print("等待上传: %ss"%wait_time)
                if wait_time >= 180:
                    print("-----等待上传超时！-----")
                    return isVisiable
                else:
                    wait_time+=1
                    sleep(1)
                    continue
    #点击开始检测按钮
    def clickBeginDetectBtn(self):
        self.find_element(*self.beginDetectBtn).click()
        sleep(2)
    #判断查看检测结果按钮是否出现，没出现则继续等待3min
    def isCheckResultBtnExist(self):
        flag = True
        #star = time()
        wait_time = 0
        while flag:
            isVisiable = super(BatchDetection, self).is_element_visible(self.checkResultBtn)
            #end = time()
            #wait_time = int(end-star)
            if isVisiable == True:
                print("-----------检测完成！-----------")
                return isVisiable
            elif isVisiable == False:
                print("等待检测: %ss"%wait_time)
                if wait_time >= 240:
                    print("----------等待检测超时！----------")
                    return isVisiable
                else:
                    wait_time+=1
                    sleep(1)
                    continue
    #获取检测成功后的相似比
    def getDetectSimilarity(self):
        return self.find_element(*self.detectSimilarity).text
    #判断是否有alert提示框
    def is_alert_exist(self):
        try:
            alert =  self.driver.switch_to_alert()
            alert.text()
            return True
        except Exception:
            return False
    #获取上传失败的弹窗提示
    def getAlertInfo(self):
        text = super(BatchDetection, self).confirm_broserAlert()
        return text
    #得到提取的篇名
    def getExtractPaperName(self):
        return self.find_element(*self.extractPaperName).text
    #得到提取的篇名
    def getExtractAuthorName(self):
        return self.find_element(*self.extractAuthorName).text
    #点击查看检测结果
    def clickCheckResultBtn(self):
        self.find_element(*self.checkResultBtn).click()
        sleep(3)
    #获取查看检测结果页面该论文所在任务的名称
    def getTaskName(self):
        return self.find_element(*self.checkResultTaskName).text
    #点击重新创建新任务按钮
    def clickReCreatBtn(self):
        self.find_element(*self.reCreatBtn).click()
        sleep(2)
    #判断是否跳回检测页面，确定任务名称按钮是否存在
    def isConfirmTaskBtnExist(self):
        flag = super(BatchDetection,self).is_element_visible(self.confirmTaskBtn)
        return flag

    '''************************************获取管理中心-账户管理下的剩余篇数信息************************************************'''

    #鼠标悬停在管理中心上
    def hoverOnManageCenter(self):
        super(BatchDetection, self).mouseHover(*self.manageCenter)
    #点击账户管理
    def clickAccountManegeTab(self):
        self.find_element(*self.accountManageTab).click()
        sleep(2)
    #得到剩余篇数
    def getRemainArticleNum(self):
        sleep(1)
        self.hoverOnManageCenter()
        self.clickAccountManegeTab()
        num = self.find_element(*self.remainArticleNum).text
        print('剩余篇数：'+num)
        return num