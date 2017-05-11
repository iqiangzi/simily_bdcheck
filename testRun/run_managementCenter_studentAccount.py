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
            print("模板已存在，模板下载成功!")

        else:
            #单击导出按钮
            stu.downloadaccount_template()
            sleep(5)
            print("模板下载成功!")
        print("下载学生账户信息模板测试成功!")
        sleep(5)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"download_studentaccount_template.jpg")

    def test_checkCount_more_run(self):
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
        stu.upload_stuaccount()
        sleep(3)

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户1.xlsx"))
        sleep(5)
        errorMessage="为1个学生账户分配"+str(a)+"篇检测数量，共需分配"+str(a)+"篇，您的可分配篇数不足，请充值后，再导入学生账户表格"


        self.assertEqual(stu.uploaderror_remind(),errorMessage)
        print("批量生成学生账户-分配检测篇数超过剩余检测篇数测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"chooseexistBatch.jpg")

    def test_choosenewBatch_exist_run(self):
        '''批量生成学生账户-新建批次已存在'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        stu.in_batchstudent()
        sleep(2)
        #选择新建批次
        stu.choose_newBatch(batchName="lytest1")
        sleep(2)
        #选择有效期
        stu.expirydate()
        sleep(2)

        self.assertEqual(stu.newBatch_error_remind(),"名称已经存在")
        print("新建批次已存在测试成功！")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"choosenewBatch_exist.jpg")

    def test_upload_TooBig_run(self):
        '''上传的文件超过5M'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("Patent_Application_Info.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"上传失败，文件过大!",msg)
        print("上传文件过大测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_TooBig.jpg")
    def test_upload_empty_run(self):
        '''上传的文件为空'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("内容为空.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"内容为空.xlsx文件解析失败",msg)
        print("上传文件内容为空测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_empty.jpg")

    def test_upload_toomany_run(self):
        '''上传文件账户超过200条'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户超过200条.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"学生账号数量超过最大限制200条",msg)
        print("上传文件账户超过限制测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_toomany.jpg")

    def test_upload_format_xls_run(self):
        '''上传的文件格式为xls'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户.xls"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号添加成功",msg)
        print("上传文件格式为.xls测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_format_xls.jpg")
    def test_upload_format_xlsx_run(self):
        '''上传的文件格式为xlsx'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户1.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号添加成功",msg)
        print("上传文件格式为.xlsx测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_format_xlsx.jpg")

    def Basic_options(self):
        '''基础选择-上传之前的公共步骤'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        stu=StudentAccount(self.driver)
        #单击进入批量生成学生账户
        stu.in_batchstudent()
        sleep(2)
        #选择已存在的批次
        stu.choose_existBatch()
        #选择账户有限期
        stu.expirydate()
        sleep(2)
        #输入账户分配检测篇数
        stu.checkcount_input(checkcount=1)
        sleep(2)
        #单击导入学生账户信息
        stu.upload_stuaccount()
        sleep(3)

    def test_uploadPaper_includeNonstandard_run(self):
        '''上传文件包含不规范账户信息'''
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户3-包含错误数据.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传文件包含不规范账户信息测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadPaper_includeNonstandard.jpg")
    def test_uploadPaper_allNonstandard_run(self):
        '''上传文件全是不规范账户信息'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()
        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户2-全是错误数据.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"学生账户2-全是错误数据.xlsx文件解析失败",msg)
        print("上传文件全是不规范账户信息测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadPaper_allNonstandard.jpg")

    def test_upload_stuaccountexist_run(self):
        '''上传的学生账户已存在'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("111.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账号已存在测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uploadPaperExist.jpg")
    def test_upload_success_run(self):
        '''上传成功'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("学生账户-规范的文件.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号添加成功",msg)
        print("上传学生账号已存在测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_success.jpg")

    def test_stuAccountName_isNull_run(self):
        '''账户名称为空'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户名称为空.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户名称为空测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountName_isNull.jpg")
    def test_stuAccountName_capital_run(self):
        '''账户名称为大写字母'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户为大写字母.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户名称为大写字母测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountName_capital.jpg")

    def test_stuAccountName_tooshort_run(self):
        '''账户名称为3位'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户名称为3位.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户名称太短测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountName_tooshort.jpg")

    def test_stuAccountName_toolong_run(self):
        '''账户名称为26位'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户名称为26位.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户名称太长测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountName_toolong.jpg")

    def test_stuAccountName_specialcharacter_run(self):
        '''账户名称为特殊字符'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户名称为特殊字符.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"账户名称为特殊字符.xlsx文件解析失败",msg)
        print("上传学生账户名称为特殊字符测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountName_specialcharacter.jpg")

    def test_stuAccountName_inchudeblank_run(self):
        '''账户名称包含空格'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户名称包含空格.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户名称包含空格测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"tuAccountName_inchudeblank.jpg")

    def test_stuAccountPassword_tooshort_run(self):
        '''账户密码为5位'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户密码为5位.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户密码长度为5位测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountPassword_tooshort.jpg")

    def test_stuAccountPassword_toolong_run(self):
        '''账户密码为21位'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户密码为21位.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户密码长度为21位测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountPassword_toolong.jpg")

    def test_stuAccountPassword_includeblank_run(self):
        '''账户密码包含空格'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户密码包含空格.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传学生账户密码包含空格测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountPassword_includeblank.jpg")

    def test_stuAccountUserName_toolong_run(self):
        '''上传文件用户名为26位'''
        #登录系统
        stu=StudentAccount(self.driver)
        self.Basic_options()

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("账户用户名为26位.xlsx"))
        sleep(5)
        msg=stu.uploaderror_remind()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"全部学生账号信息不规范或该账号已存在",msg)
        print("上传文件用户名长度超出限制测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"stuAccountUserName_toolong.jpg")

    '''
    #备注：目前插件版本太低，不是规定的格式不会进行任何操作
    def test_upload_formaterror_run(self):
        #上传文件格式不是xls或xlsx
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
        stu.upload_stuaccount()
        sleep(3)

        #调用autoIt生成的上传文件应用
        stu.uploadFile_para("chrome",stu.getFilePath("general.txt"))
        sleep(5)
        msg=stu.getWinAlert()
        #print(msg)
        self.assertEqual(stu.uploaderror_remind(),"内容为空.xlsx文件解析失败",msg)
        print("上传文件类型不是规定类型测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"upload_formaterror.jpg")
'''









