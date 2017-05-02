#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : accountManagement.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class AccountManagement(BasePage):

    #管理中心
    manageCenter_button_loc=(By.ID,"manageCenter")
    #账户管理
    accountManage_button_loc=(By.XPATH,".//*[@id='manageCenterList']/li[1]/a")

    #新建子账户
    createUser_button_loc=(By.ID,"create-user")
    #子账户名称
    create_accountName_loc=(By.ID,"accountName")
    #密码
    create_password_loc=(By.ID,"password")
    #再次输入密码
    create_repassword_loc=(By.ID,"rePassword")
    #单位名称
    create_displayName_loc=(By.ID,"displayName")
    #分配检测篇数
    create_checkQuantity_loc=(By.ID,"checkQuantity")
    #确定创建按钮
    confirm_button_loc=(By.ID,"confirmCreateBtn")
    #子账户名称错误提示
    createError_remind_loc=(By.ID,"validateTips")


    #查询按钮
    select_button_loc=(By.XPATH,"html/body/div[4]/div[3]/form/div[2]/input")
    #查询账户名称
    select_UserName_loc=(By.ID,"userIdInput")
    #查询错误提示
    selectError_remind_loc=(By.ID,"errorTip")


    #导出按钮
    export_button_loc=(By.XPATH,"html/body/div[4]/div[3]/button")

    #账户名称链接
    userName_link_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr[2]/td[1]/a")
    #操作-分配篇数
    operation_checkQuantity_loc=(By.ID,"2_allotCheckQuantity")
    #分配篇数
    checkCount_Input_loc=(By.ID,"checkCountInput")
    #可分配篇数
    checkCount_Tip_loc=(By.ID,"CheckCountTip")
    #确定分配
    confirm_modifyCount_loc=(By.ID,"confirmAllot")
    #取消分配
    cancel_modifyCount_loc=(By.ID,"blueBtnsmal")
    #操作-修改密码
    operation_updatePassword_loc=(By.ID,"2_updatePassword")
    #新密码
    newPassword_loc=(By.ID,"newPassword")
    #确认新密码
    renewPassword_loc=(By.ID,"renewPassword")
    #确定修改密码
    confirm_updatePassword_loc=(By.ID,"confirmUpdatePasswordBtn")
    #操作-关闭/开通
    operation_lock_loc=(By.ID,"2_lock")
    #关闭账户提示信息
    lockAccount_remind_loc=(By.XPATH,".//*[@id='confirmUpAccountDialog']/p")
    #直接关闭账户
    closeAccount_button_loc=(By.ID,"closeAccount")
    #分配后关闭
    closeafter_distribution_loc=(By.XPATH,".//*[@id='confirmUpAccountDialog']/div/button[2]")
    #提示窗口关闭
    close_remindwindow_loc=(By.XPATH,"html/body/div[12]/div[1]/button")
    #关闭/开通账号提示
    alertMessage_remind_loc=(By.ID,"alertMessage_p")
    #信息管理页面
    informationManage_title_loc=(By.XPATH,"html/body/div[4]/div[2]/div/span[2]/b")




    def in_accountManage(self):

        #鼠标悬停在账户管理上，然后单击子账户信息
        above=self.find_element(*self.manageCenter_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        self.find_element(*self.accountManage_button_loc).click()

    def create_ChildAccount_button(self):
        '''创建子账户按钮'''
        self.find_element(*self.createUser_button_loc)

    def create_childAccount(self,childname,password,repassword,displayname,checkquanrity):
        '''创建子账户'''
        self.create_childAccountName(childname)
        self.create_password(password)
        self.create_repassword(repassword)
        self.create_displayName(displayname)
        self.create_checkQuantity(checkquanrity)

    def create_childAccountName(self,childname):
        '''创建子账户名称'''
        self.find_element(*self.create_accountName_loc).clear()
        self.find_element(*self.create_accountName_loc).send_keys(childname)

    def create_password(self,password):
        '''创建子账户密码'''
        self.find_element(*self.create_password_loc).clear()
        self.find_element(*self.create_password_loc).send_keys(password)
    def create_repassword(self,repassword):
        '''创建子账户再次输入密码'''
        self.find_element(*self.create_repassword_loc).clear()
        self.find_element(*self.create_repassword_loc).send_keys(repassword)
    def create_displayName(self,displayname):
        '''创建子账户单位名称'''
        self.find_element(*self.create_displayName_loc).clear()
        self.find_element(*self.create_displayName_loc).send_keys(displayname)
    def create_checkQuantity(self,checkquantity):
        '''创建子账户分配检测篇数'''
        self.find_element(*self.create_checkQuantity_loc).clear()
        self.find_element(*self.create_checkQuantity_loc).send_keys(checkquantity)

    def confirm_create_button(self):
        '''确定创建按钮'''
        self.find_element(*self.confirm_button_loc).click()
    def createAccount_error_remind(self):
        '''创建子账户错误提示'''
        return self.find_element(*self.createError_remind_loc).text
    def select_button(self):
        '''查询按钮'''
        self.find_element(*self.select_button_loc).click()
    def selectAccount_input(self,accountname):
        '''输入查询账户'''
        self.find_element(*self.select_UserName_loc).clear()
        self.find_element(*self.select_UserName_loc).send_keys(accountname)
    def select_error_remind(self):
        '''查询失败提示'''
        return self.find_element(*self.selectError_remind_loc).text


    def export_button(self):
        '''导出按钮'''
        self.find_element(*self.export_button_loc).click()

    def operation_checkQuantity_button(self):
        '''分配篇数'''
        self.find_element(*self.operation_checkQuantity_loc).click()
    def checkCount_input(self,checkcount):
        '''分配篇数'''
        self.find_element(*self.checkCount_Input_loc).clear()
        self.find_element(*self.checkCount_Input_loc).send_keys(checkcount)
    def confirm_modifyCount(self):
        '''确定分配篇数'''
        self.find_element(*self.confirm_modifyCount_loc).click()
    def cancel_modifyCount(self):
        '''取消分配篇数'''
        self.find_element(*self.cancel_modifyCount_loc).click()
    def checkCount_tip(self):
        '''可分配篇数'''
        return self.find_element(*self.checkCount_Tip_loc).text


    def modify_password_button(self):
        '''修改密码'''
        self.find_element(*self.operation_updatePassword_loc).click()
    def modify_newPassword(self,newpassword):
        '''新密码'''
        self.find_element(*self.newPassword_loc).clear()
        self.find_element(*self.newPassword_loc).send_keys(newpassword)
    def modify_renewPassword(self,renewpassword):
        '''确认新密码'''
        self.find_element(*self.renewPassword_loc).clear()
        self.find_element(*self.renewPassword_loc).send_keys(renewpassword)

    def confrim_modifyPassword(self):
        '''确认修改密码'''
        self.find_element(*self.confirm_updatePassword_loc).click()

    def account_link(self):
        '''账户链接'''
        self.find_element(*self.userName_link_loc).click()
    def account_status_button(self):
        '''账户状态操作-开通/关闭'''
        self.find_element(*self.operation_lock_loc).click()
    def close_account_remind(self):
        '''关闭账户信息提示'''
        return self.find_element(*self.lockAccount_remind_loc).text
    def close_after_distribution(self):
        '''分配篇数后关闭'''
        self.find_element(*self.closeafter_distribution_loc).click()
    def close_account_button(self):
        '''直接关闭'''
        self.find_element(*self.closeAccount_button_loc).click()
    def alertMessage_remind(self):
        '''账户状态操作提示'''
        return self.find_element(*self.alertMessage_remind_loc).text
    def informationManage_title(self):
        '''信息管理页面标题'''
        return self.find_element(*self.informationManage_title_loc).text





