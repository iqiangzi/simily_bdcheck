#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-02 10:01:51
# @Author  : Cys
# @Site    : 
# @File    : manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
from selenium.webdriver.common.by import By
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
    oldTaskAlert = (By.CSS_SELECTOR,'#oldTaskAlert>.colRed') #输入已有任务的错误提示
    creatTaskALert = (By.CSS_SELECTOR,'#creatTaskAlert>.colRed') #创建新任务错误提示
    confirmTaskBtn = (By.CSS_SELECTOR,'#confirmTaskNameBtn') #确认任务名称按钮
    creatTaskName = (By.CSS_SELECTOR,'.collereTask>.taskName') #新建任务名称确认
    modifyTaskName = (By.CSS_SELECTOR,'.collereTask>#reNewTaskName') #修改任务名称按钮
    rechoiseBtn = (By.CSS_SELECTOR,'.collereTask>#reChoseOldTask') #重新选择任务按钮
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
        sleep(1)
    #选择已有任务
    def clickOldTaskchoise(self):
        old_name = self.find_element(*self.oldTaskchoise).text
        sleep(2)
        self.find_element(*self.oldTaskchoise).click()
        sleep(2)
        return old_name
    #点击新建任务选择框
    def clickChooseBtn1(self):
        self.find_element(*self.chooseBtn1).click()
        sleep(2)
    #输入已存在的任务名称
    def inputSameName(self):
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








