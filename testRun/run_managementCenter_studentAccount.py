#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Nxy
# @Site    : 
# @File    : run_studentAccount.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import sleep
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.managementCenter.basePagestudentAccount import UserVer
from testCase.models.managementCenter.studentAccount import StudentAccount
from testResult.getResultImage import getResultImage
import os

class RunStudentAccount(myUnitChrome.UnitChrome):

    def test_downloadtemplate_run(self):
        '''下载学生账户模板成功'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        stu.in_batchstudent()
        sleep(2)

        flag=stu.verifyExist()

        if flag is True:
            stu.renameFileName()
            stu.downloadaccount_template()
            sleep(5)
            print("模板已存在，模板下载成功")

        else:
            #单击导出按钮
            stu.downloadaccount_template()
            sleep(5)
            print("模板下载成功")

        sleep(5)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"download_studentaccount_template.jpg")

    def test_chooseexistBatch_run(self):
        '''批量生成学生账户-分配检测篇数超过剩余检测篇数'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        stu.in_batchstudent()
        sleep(2)
        stu.choose_existBatch()
        stu.expirydate()
        sleep(2)
        a=stu.checkcount_surplus()+1
        print(a)
        stu.checkcount_input(checkcount=a)
        sleep(2)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"chooseexistBatch.jpg")
    def test_choosenewBatch_run(self):
        '''批量生成学生账户-新建批次'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        stu.in_batchstudent()
        sleep(2)
        stu.choose_newBatch(batchName="newbatch1")
        sleep(2)

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"choosenewBatch.jpg")
    def test_upload_run(self):
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        stu.in_batchstudent()
        sleep(2)
        stu.choose_existBatch()
        stu.expirydate()
        sleep(2)

        stu.checkcount_input(checkcount=1)
        sleep(2)
        print("基本条件输入成功")
        stu.upload_stuaccount()
        sleep(3)

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("111.xlsx"))
        sleep(5)
        #msg=stu.getWinAlert()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在")
        print("上传成功")


        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadPaperExist.jpg")







