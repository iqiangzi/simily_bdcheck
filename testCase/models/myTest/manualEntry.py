#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-02 10:01:51
# @Author  : Cys
# @Site    : 
# @File    : manualEntry.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from util.commonUtils.fileOption import FilesOption
from util.toolUtils.getPath import GetPath
from testCase.pageObj.basePage import BasePage
from time import sleep,strftime


class ManualEntry(BasePage):
    #获取页面元素位置
    myTestTab = (By.CSS_SELECTOR,'#myCheck>a')  #顶部导航栏-我的检测
    manualDetectButton = (By.CSS_SELECTOR,'.colleManualbtn')    #手工检测按钮
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

    #检测内容相关***********************************************************************************************
    paperName = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#paperName') #检测内容-篇名
    authorName = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#authorName') #检测内容-作者
    authorCompany = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#authorCompany') #检测内容-作者单位
    majority = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#majority') #检测内容-专业
    tutor = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#tutor') #检测内容-导师
    paperContent = (By.CSS_SELECTOR,'.colleSerch>.colletaskName>#paperContent') #检测内容-录入内容
    beginDetectBtn = (By.CSS_SELECTOR,'#beginCheck') #开始检测按钮
    detectState = (By.CSS_SELECTOR,'#uploadPaperList>table>tbody>tr:nth-child(2)>.checkstate') #开始检测状态
    detectSimilarity = (By.CSS_SELECTOR,'#uploadPaperList>table>tbody>tr:nth-child(2)>.similarity') #检测页面的相似比
    checkResultBtn = (By.CSS_SELECTOR,'#checkResult') #查看检测结果按钮
    reCreatBtn = (By.CSS_SELECTOR,'#reCreat') #继续创建新任务按钮
    mytestDetectState = (By.CSS_SELECTOR,'.collegeTable>tbody>tr:nth-child(2)>#forstate') #我的检测列表检测状态
    checkResultTaskName = (By.CSS_SELECTOR,'.paperLguide>b') #查看检测结果页面的任务名称

    #检测结果页面确认***********************************************************************************************

    accountManageTab = (By.CSS_SELECTOR,'#manageCenterList>li:nth-child(1)>a') #账号管理导航按钮
    manageCenter= (By.CSS_SELECTOR,'#manageCenter>a') #管理中心按钮
    remainArticleNum = (By.CSS_SELECTOR,'#surplusCheckCount') #剩余篇数

    #点击我的检测
    def clickMyTes(self):
        self.find_element(*self.myTestTab).click()
        sleep(2)
    #点击手工录入按钮
    def clickManualDetectButton(self):
        self.find_element(*self.manualDetectButton).click()
        sleep(3)
    #输入新建任务名称
    def inputCreatTaskBox(self,task_name):
        self.find_element(*self.creatTaskBox).clear()
        self.find_element(*self.creatTaskBox).send_keys(task_name)
        sleep(2)
    #获取新建任务时的不重名称
    def getDifferName(self):
        tag=strftime("%Y-%m-%d %H_%M_%S")
        name="手工录入%s"%(tag)
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
        super(ManualEntry, self).is_element_visible(self.creatTaskALert)
    #获取选择已有任务时的错误提示
    def getOldTaskAlert(self):
        return  self.find_element(*self.oldTaskAlert).text
    #判断选择已有任务时的错误提示是否存在，如果存在返回flag=true，否则返回false
    def isOldAlertExist(self):
        flag = super(ManualEntry, self).is_element_visible(self.oldTaskAlert)
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
        flag = super(ManualEntry,self).is_element_clickable(self.oldTaskchoise1)
        #print(flag)
        return flag
    #手工录入过程
    def manualEntryProcess(self):
        self.find_element(*self.manualDetectButton).click()
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
    #手工录入输入篇名
    def inputPaperName(self,papaername):
        name = strftime("%Y-%m-%d %H_%M_%S")
        self.find_element(*self.paperName).clear()
        self.find_element(*self.paperName).send_keys(papaername+"_"+name)
        sleep(1)
    #手工录入作者名称
    def inputAuthorName(self,authorname):
        self.find_element(*self.authorName).clear()
        self.find_element(*self.authorName).send_keys(authorname)
        sleep(1)
    #手工录入作者单位
    def inputAuthorCompany(self,company):
        self.find_element(*self.authorCompany).clear()
        self.find_element(*self.authorCompany).send_keys(company)
        sleep(1)
    #手工录入作者专业
    def inputMajority(self,majority):
        self.find_element(*self.majority).clear()
        self.find_element(*self.majority).send_keys(majority)
        sleep(1)
    #手工录入作者导师
    def inputTutor(self,tutor):
        self.find_element(*self.tutor).clear()
        self.find_element(*self.tutor).send_keys(tutor)
        sleep(1)
    #手工录入论文内容
    def inputPaperContent(self,filename):
        #self.find_element(*self.paperContent).clear()
        #self.find_element(*self.paperContent).send_keys(Keys.TAB)
        self.find_element(*self.paperContent).send_keys(filename)
        #sleep(10)
    #逐行读取文本内容并逐行写入文本框
    def readAndInputContent(self,filename):
        f = FilesOption()
        g = GetPath()
        manu = ManualEntry(self.driver)
        filePath =g.getAbsoluteFilePath(filename,r"detectPaper\%s"%filename)
        print(filePath)
        Flist = f.readFileContent(filePath)
        #self.ManualNoText("文本信息正确开始检测","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('gbk')
            con=con.replace("\t","")
            manu.inputPaperContent(con)
        sleep(2)
    #点击开始检测按钮
    def clickBeginDetectBtn(self):
        self.find_element(*self.beginDetectBtn).click()
        sleep(2)

    '''**********************************************开始检测论文**********************************************************'''

    #获取开始检测状态文本
    def getDetectState(self):
        return self.find_element(*self.detectState).text
    #获取检测成功后的相似比
    def getDetectSimilarity(self):
        return self.find_element(*self.detectSimilarity).text
    #判断查看检测结果按钮是否出现，没出现则继续等待3min
    def isCheckResultBtnExist(self):
        flag = True
        #star = time()
        wait_time = 0
        while flag:
            isVisiable = super(ManualEntry, self).is_element_visible(self.checkResultBtn)
            #end = time()
            #wait_time = int(end-star)
            if isVisiable == True:
                print("-----------检测完成！-----------")
                return isVisiable
            elif isVisiable == False:
                print("等待检测: %ss"%wait_time)
                if wait_time >= 180:
                    print("----------等待检测超时！----------")
                    return isVisiable
                else:
                    wait_time+=1
                    sleep(1)
                    continue
    #判断是否有alert弹窗
    def verifyExistAlert(self):
        text = super(ManualEntry,self).confirm_broserAlert()
        print(text)
        return text
    #输入大文本内容
    def readAndInputBigData(self,filename,fieldname):
        f = FilesOption()
        g = GetPath()
        manu = ManualEntry(self.driver)
        filePath =g.getAbsoluteFilePath(filename,r"detectPaper\%s"%filename)
        print(filePath)
        Flist = f.readFileContent(filePath)
        #self.ManualNoText("文本信息正确开始检测","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('gbk')
            con=con.replace("\t","")
            if fieldname == "paperName":
                manu.inputPaperName(con)
            elif fieldname == "authorName":
                manu.inputAuthorName(con)
            elif fieldname == "authorCompany":
                manu.inputAuthorCompany(con)
            elif fieldname == "majority":
                manu.inputMajority(con)
            elif fieldname == "tutor":
                manu.inputTutor(con)
        sleep(2)
    #判断是否有提示框
    def is_alert_exist(self):
        try:
            super(ManualEntry,self).confirm_broserAlert()
            return True
        except Exception:
            return False
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
        flag = super(ManualEntry,self).is_element_visible(self.confirmTaskBtn)
        return flag

    '''************************************获取管理中心-账户管理下的剩余篇数信息************************************************'''

    #鼠标悬停在管理中心上
    def hoverOnManageCenter(self):
        super(ManualEntry, self).mouseHover(*self.manageCenter)
    #点击账户管理
    def clickAccountManegeTab(self):
        self.find_element(*self.accountManageTab).click()
        sleep(2)
    #得到剩余篇数
    def getRemainArticleNum(self):
        self.hoverOnManageCenter()
        self.clickAccountManegeTab()
        num = self.find_element(*self.remainArticleNum).text
        print('剩余篇数：'+num)
        return num


if __name__=="__main__":
   ManualEntry(BasePage).getOverLongName()








