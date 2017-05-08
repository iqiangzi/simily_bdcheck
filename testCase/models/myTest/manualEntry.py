#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-02 10:01:51
# @Author  : Cys
# @Site    : 
# @File    : manualEntry.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from util.commonUtils.fileOption import FilesOption
from util.toolUtils.getPath import GetPath
from testCase.pageObj.basePage import BasePage
from time import sleep,strftime
from util.toolUtils.txtOption import TxtOption

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
    checkResultBtn = (By.CSS_SELECTOR,'#checkResult') #查看检测结果按钮
    reCreatBtn = (By.CSS_SELECTOR,'#reCreat') #继续创建新任务按钮
    mytestDetectState = (By.CSS_SELECTOR,'.collegeTable>tbody>tr:nth-child(2)>#forstate') #我的检测列表检测状态

    #检测结果页面确认***********************************************************************************************


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
        long_name*=41
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
        self.find_element(*self.oldTaskchoise).click()
        sleep(2)
        self.find_element(*self.confirmTaskBtn).click()
        sleep(2)
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
        filePath =g.getAbsoluteFilePath(filename,r"detectPaper\detect_file.txt")
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
    #获取开始检测状态文本
    def getDetectState(self):
        return self.find_element(*self.detectState).text


if __name__=="__main__":
   ManualEntry(BasePage).getOverLongName()








