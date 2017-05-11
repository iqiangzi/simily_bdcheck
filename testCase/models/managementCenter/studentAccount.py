#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    : 
# @File    : studentAccount.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
from testCase.models.managementCenter.basePagestudentAccount import BasePage
import time
from time import sleep
from selenium.webdriver.common.by import By
import os
from util.toolUtils.getPath import GetPath

class StudentAccount(BasePage):

    #批量生成学生账户
    batchstudent_accounts_loc=(By.XPATH,"html/body/div[4]/div[2]/div/div/a/span")
    #已存在批次
    existBatch_choose_loc=(By.ID,"existBatch")
    #已存在批次下拉列表
    existBatch_list_loc=(By.XPATH,".//*[@id='select-box']/a")
    #选择第一个批次
    fristBatch_choose_loc=(By.XPATH,".//*[@id='select-box']/ul/li[1]")
    #新建批次
    newBatch_choose_loc=(By.ID,"newBatch")
    #新建批次名称
    newBatch_input_loc=(By.ID,"batchName")
    #新建批次错误信息提示
    newBatch_errorremind_loc=(By.ID,"newBatchErr")
    #有效期日期
    expirydate_button_loc=(By.XPATH,"html/body/div[4]/div[2]/div[2]/div[2]/span/img")
    #选择一个有效日期
    expirydate_choose_loc=(By.XPATH,".//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[3]/a")
    #检测篇数
    checkCount_input_loc=(By.ID,"jine")
    #剩余检测篇数
    checkCount_surplus_loc=(By.ID,"shengyujine")
    #下载学生账户信息模板
    download_stuaccount_template=(By.XPATH,"html/body/div[4]/div[2]/div[2]/p/a")
    #导入学生账户信息
    upload_stuaccount_loc=(By.XPATH,".//*[@id='addOK']/div[2]/label")
    #导入学生账户失败
    uploaderror_remind_loc=(By.XPATH,"html/body/div[4]/div[2]/div[3]/h3")


    #单击进入批量生成学生账户
    def in_batchstudent(self):
        self.find_element(*self.batchstudent_accounts_loc).click()
    #选择已存在的批次
    def choose_existBatch(self):

        self.find_element(*self.existBatch_choose_loc).click()
        sleep(2)
        self.find_element(*self.existBatch_list_loc).click()
        sleep(2)
        self.find_element(*self.fristBatch_choose_loc).click()
    #新建批次
    def choose_newBatch(self,batchName):
        self.find_element(*self.newBatch_input_loc).clear()
        self.find_element(*self.newBatch_input_loc).send_keys(batchName)

    def newBatch_error_remind(self):
        return self.find_element(*self.newBatch_errorremind_loc).text

    #选择有效期
    def expirydate(self):
        self.find_element(*self.expirydate_button_loc).click()
        sleep(2)
        self.find_element(*self.expirydate_choose_loc).click()
    #下载学生账户信息模板
    def downloadaccount_template(self):
        self.find_element(*self.download_stuaccount_template).click()
    #分配检测篇数
    def checkcount_input(self,checkcount):
        self.find_element(*self.checkCount_input_loc).clear()
        self.find_element(*self.checkCount_input_loc).send_keys(checkcount)
    #剩余分配篇数
    def checkcount_surplus(self):
        count=self.find_element(*self.checkCount_surplus_loc).text
        count=int(count)
        return count
    def upload_stuaccount(self):
        self.find_element(*self.upload_stuaccount_loc).click()

    #判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName(self):
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        if os.listdir(dir_path):
            os.rename(dir_path+"\学生账户信息模板.xlsx",dir_path+r"\%s.xlsx"%(name))

        else:
            pass

    def verifyExist(self):
        #判断是否下载到本地,返回bool类型的True或False
        #判断文件是否存在
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        flag = os.path.exists(dir_path+"\学生账户信息模板.xlsx")
        return flag

    #调用autoit生成的exe，并传入浏览器、需要上传至页面文件的地址两个参数
    def uploadFile_para(self,browserName,filePath):
        #注意路径中不能存在空格并且文件夹名称不能过长
        ab_path = GetPath().getAbsoluteFilePath("testvb.exe",r"uploadApp\testvb.exe")
        #os.system("./../testData/massProduceUploadApps/testvb.exe"+ " "+browserName+" "+filePath)
        #print(ab_path+ " "+browserName+" "+filePath)
        #print('''"%s" "%s" "%s"''' % (ab_path,browserName,filePath))
        #os.system('''"%s" "%s" "%s"'''% (ab_path,browserName,filePath))
        os.system(ab_path+ " "+browserName+" "+filePath)

    #获取上传文件的绝对路径
    def getFilePath(self,filename):
        file_path = GetPath().getAbsoluteFilePath("%s"%filename,r"studentsAccountUploadTestData\%s"%filename)
        return file_path

    def getWinAlert(self):
        return super(StudentAccount,self).confirm_broserAlert()
        #BasePage.confirm_broserAlert()
    def uploaderror_remind(self):
        return self.find_element(*self.uploaderror_remind_loc).text





