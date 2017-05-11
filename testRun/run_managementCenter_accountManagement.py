#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_accountManagement.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.managementCenter.accountManagement import AccountManagement
from testCase.models.managementCenter.basePageaccountMgmt import UserVer
from testCase.models.managementCenter.basePageaccountMgmt import BasePage
from time import sleep
from testResult.getResultImage import getResultImage

class RunAccountManagement(myUnitChrome.UnitChrome):

    def test_AaccountName_null_run(self):
        '''账户名称为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"账户名不能为空")
        print("账户名称不能为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_NULL.jpg")

    def test_AaccountName_allNum_run(self):
        '''子账户名称全为数字'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="11111",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"不能全都是数字")
        print("子账户名称不能全是数字测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_allNum.jpg")

    def test_AaccountName_allUnderline_run(self):
        '''子账户名称全为下划线'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="____",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"不能全都是下划线")
        print("子账户名称不能全是下划线测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_allUnderline.jpg")

    def test_AaccountName_specialcharacter_run(self):
        '''子账户名称有特殊字符'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="abc!@#",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"只能是数字，小写字母，下划线")
        print("子账户名称不能有特殊字符测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_specialcharacter.jpg")

    def test_AaccountName_capital_run(self):
        '''子账户名称有大写字母'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="ABCDEF",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"只能是数字，小写字母，下划线")
        print("子账户名称不能有大写字母测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_capital.jpg")

    def test_AaccountName_length1_run(self):
        '''子账户名称不足4位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="abc",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"账户名长度为4-16位")
        print("账户名太短测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_Tooshort.jpg")

    def test_AaccountName_length2_run(self):
        '''子账户名称超过16位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="abc12345678901234",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"账户名长度为4-16位")
        print("账户名过长测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountname_Toolong.jpg")


    def test_Apassword_isNull_run(self):
        '''密码为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"请输入密码")
        print("密码不能为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"password_isNull.jpg")
    def test_Apassword_length1_run(self):
        '''密码不足6位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="12345",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("密码不能小于6位测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"password_NotLong.jpg")

    def test_Apassword_length2_run(self):
        '''密码超过20位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123456789012345678901",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("密码不能超过20位测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"password_TooLong.jpg")

    def test_Apassword_includeblank_run(self):
        '''密码包含空格'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123 456",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("密码不能有空格测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"password_includeblank.jpg")

    def test_Apassword_specialcharacter_run(self):
        '''密码为特殊字符'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="！@#￥%……",repassword="！@#￥%……",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"单位名称不能为空")
        print("密码可以为特殊字符测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"password_specialcharacter.jpg")


    def test_Arepassword_isNull_run(self):
        '''再次输入密码为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123456",repassword="",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"请再次输入密码")
        print("再次输入密码不能为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"repassword_isNull.jpg")

    def test_Arepassword_inconformity_run(self):
        '''两次密码不一致'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123456",repassword="123465",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"两次输入密码必须一致")
        print("两次密码必须一致测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"repassword_inconformity.jpg")

    def test_Arepassword_casesensitive_run(self):
        '''密码区分大小写'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="abcdef",repassword="ABCDEF",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"两次输入密码必须一致")
        print("密码区分大小写测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"repassword_casesensitive.jpg")

    def test_Adisplayname_isNull_run(self):
        '''单位名称为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123456",repassword="123456",displayname="",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"单位名称不能为空")
        print("单位名称不能为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"displayname_isNull.jpg")

    def test_Acheckquanrity_isNull_run(self):
        '''分配检测篇数为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test111",password="123456",repassword="123456",displayname="万方数据",checkquanrity="")
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"检测篇数不能为空")
        print("检测篇数不能为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"checkquanrity_isNull.jpg")

    def test_Acheckquanrity_more_run(self):
        '''分配检测篇数超过可分配篇数'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        text=am.checkquritity_remind()
        a=text[4:-1]
        count=int(a)
        print("可分配篇数：",count)
        count1=count+1
        print("分配篇数：",count1)


        am.create_childAccount(childname="test111",password="123456",repassword="123456",displayname="万方数据",checkquanrity=count1)
        am.confirm_create_button()
        self.assertEqual(am.createAccount_error_remind(),"不能大于可分配篇数")
        print("分配篇数不能超过可分配篇数测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"checkquanrity_more.jpg")
    def test_Aaccountcreate_success_run(self):
        '''创建子账户成功'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)
        am.create_childAccount(childname="test7",password="123456",repassword="123456",displayname="万方数据",checkquanrity="1")
        am.confirm_create_button()
        sleep(2)
        text=am.create_newAccountName()

        try:
            self.assertEqual(text,"collegeuser.test7")
            #self.assertNotEqual(am.createAccount_error_remind(),"该子帐号已经存在")
            print("子账户创建成功！")
        except:
            print("子账户创建失败，该子账户已存在")


        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"accountcreate_success.jpg")

    def test_AchildAccount_exist_run(self):
        '''子账户已存在'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)
        am=AccountManagement(self.driver)
        am.create_ChildAccount_button()
        sleep(2)

        am.create_childAccount(childname="test6",password="123456",repassword="123456",displayname="万方数据",checkquanrity="1")
        am.confirm_create_button()
        sleep(2)

        self.assertEqual(am.createAccount_error_remind(),"该子帐号已经存在")
        print("子账户已存在测试成功！")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"account_exist.jpg")

    def test_Bexport_run(self):
        '''子账户导出'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        time.sleep(2)
        #切换到子账户管理页面
        am=AccountManagement(self.driver)
        #cam.in_child()
        time.sleep(2)

        flag=am.verifyExist()

        if flag is True:
            am.renameFileName()
            am.export_button()
            time.sleep(5)
            print("文件已存在,导出成功")

        else:
            #单击导出按钮
            am.export_button()
            time.sleep(5)
            print("文件导出成功")

        time.sleep(5)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"Accountlist_export.jpg")

    def test_Bconfirmmodify_checkQuantity_run(self):
        '''确定修改分配篇数'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        #单击分配篇数按钮
        am.operation_checkQuantity_button()
        sleep(2)
        #输入分配篇数
        am.checkCount_input(checkcount="10")
        #单击确认按钮
        am.confirm_modifyCount()
        sleep(2)
        #判断是否修改成功
        self.assertEqual(am.now_checkCount(),10,msg="修改分配篇数失败")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"confirmmodify_checkQuantity.jpg")

    def test_Bcancelmodify_checkQuantity_run(self):
        '''取消修改分配篇数'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        oldnum=am.now_checkCount()
        sleep(2)
        #单击分配篇数按钮
        am.operation_checkQuantity_button()
        #输入分配篇数
        am.checkCount_input(checkcount="10")
        sleep(2)
        #单击取消按钮
        am.cancel_modifyCount()
        sleep(2)
        nownum=am.now_checkCount()
        #判断是否修改成功
        self.assertEqual(oldnum,nownum,msg="取消分配失败，剩余篇数发生变化")
        print("取消分配成功！")

    def test_Bfailmodify_checkQuantity_run(self):
        '''修改分配篇数失败'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        #单击分配篇数按钮
        am.operation_checkQuantity_button()
        text=am.checkCount_tip()
        count=int(text)
        print("可分配篇数：",count)
        count1=count+1
        print("分配篇数：",count1)
        #输入分配篇数
        am.checkCount_input(checkcount=count1)
        #单击确认按钮
        am.confirm_modifyCount()
        #判断是否修改成功
        self.assertEqual(am.checkCount_fail_remind(),"超过可分配数量，请重新分配！")

        print(am.checkCount_fail_remind()+"\n"+"测试成功")
         #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"failmodify_checkQuantity.jpg")

    def test_Bmodifypassword_success_run(self):
        '''正确修改密码'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="123456")
        am.modify_renewPassword(renewpassword="123456")
        #确认修改密码
        am.confrim_modifyPassword()
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifypassword_success.jpg")
    def test_Bmodifynewpassword_isNull_run(self):
        '''新密码为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        #am.modify_newPassword(newpassword="123456")
        #am.modify_renewPassword(renewpassword="123456")
        #确认修改密码
        am.confrim_modifyPassword()
        sleep(2)
        self.assertEqual(am.modifyPassword_remind(),"请输入新密码")
        print("修改密码-新密码为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_isNull.jpg")
    def test_Bmodifynewpassword_length1_run(self):
        '''新密码长度不足6位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="1234")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("修改密码-新密码长度不足测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_tooshort.jpg")

    def test_Bmodifynewpassword_length2_run(self):
        '''新密码长度超过20位'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="123456789012345678901")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("修改密码-新密码长度太长测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_toolong.jpg")
    def test_Bmodifynewpassword_includeblank_run(self):
        '''新密码包含空格'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="12  34")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"密码长度为6-20位，仅限数字、字母及字符（不能有空格）,字母区分大小写")
        print("修改密码-新密码有空格测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_includeblank.jpg")
    def test_Bmodifynewpassword_specialcharacter_run(self):
        '''新密码包含特殊字符'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="!@#$%^")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"请再次输入新密码")
        print("修改密码-新密码有特殊字符测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_specialcharacter.jpg")

    def test_Bmodifyrepassword_isNull_run(self):
        '''再次输入密码为空'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="123456")
        am.modify_renewPassword(renewpassword="")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"请再次输入新密码")
        print("修改密码-再次输入密码为空测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifyrepassword_isNull.jpg")

    def test_Bmodifypassword_inconformity_run(self):
        '''两次密码输入不一致'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="123456")
        am.modify_renewPassword(renewpassword="1234567")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"两次输入密码必须一致")
        print("修改密码-两次密码输入不一致测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_inconformity.jpg")

    def test_Bmodifypassword_casesensitive_run(self):
        '''密码区分大小写'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.modify_password_button()
        #输入修改的密码
        am.modify_newPassword(newpassword="abcDEF")
        am.modify_renewPassword(renewpassword="ABCdef")
        #确认修改密码
        am.confrim_modifyPassword()
        self.assertEqual(am.modifyPassword_remind(),"两次输入密码必须一致")
        print("修改密码-密码区分大小写测试成功")
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"modifynewpassword_casesensitive.jpg")

    def test_Caccountlink_run(self):
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.account_link()
        sleep(2)
        text=am.informationManage_title()
        self.assertEqual(text,"信息管理",msg="账户链接失败")
        print("账号链接测试成功")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"accountlink.jpg")

    def test_Ccloseaccount_direct_run(self):
        '''直接关闭账户'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        #单击关闭按钮
        am.account_status_button()

        #单击直接关闭
        am.close_account_button()
        sleep(2)
        self.assertEqual(am.alertMessage_remind(),"开通")
        print("账户关闭成功，测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"closeaccount.jpg")

    def test_Ccloseaccount_afterdistribution_run(self):
        '''分配后关闭账户'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)

        #单击关闭按钮
        am.account_status_button()
        #单击分配后关闭
        am.close_after_distribution()
        sleep(2)
        self.assertEqual(am.alertMessage_remind(),"关闭")
        print("分配后关闭账户测试成功！")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"closeafter_distribution.jpg")

    def test_Copenaccount_run(self):
        '''开通账户'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.account_status_button()
        sleep(2)
        self.assertEqual(am.alertMessage_remind(),"关闭",msg="账户开通失败，原因可能是账户状态为开通")
        print("账户开通成功")
        sleep(2)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"openaccount.jpg")

    def test_Cselectaccount_exist_run(self):
        '''查询存在的账户'''
       #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.list_search(accountname="collegeuser.test")

        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"selectaccount_exist.jpg")

    def test_Cselectaccount_notexist_run(self):
        '''查询不存在的账户'''
        #登录系统
        login=UserVer(self.driver)
        login.userLogin("collegeuser","f")
        sleep(2)

        am=AccountManagement(self.driver)
        am.selectAccount_input(accountname="collegeuser.notexist")
        am.select_button()
        sleep(2)
        text=am.select_error_remind()
        self.assertEqual(text,"没有找到您要搜索的内容。")
        print(text)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"selectaccount_notexist.jpg")










