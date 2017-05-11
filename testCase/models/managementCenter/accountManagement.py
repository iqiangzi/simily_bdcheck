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
import os
from util.toolUtils.getPath import GetPath


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
    #可分配篇数注释
    checkQuantity_remind_loc=(By.XPATH,".//*[@id='dialog-form']/p[6]/span[2]")
    #新建账户名称
    newAccount_name_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr[3]/td[1]/a")



    #查询按钮
    #select_button_loc=(By.XPATH,"html/body/div[4]/div[3]/form/div[2]/input")
    select_button_loc=(By.CLASS_NAME,"blueBtnsmal")
    #查询账户名称
    select_UserName_loc=(By.ID,"userIdInput")
    #查询错误提示
    selectError_remind_loc=(By.XPATH,"html/body/div[4]/div[3]/p")
    #查询到的账户名
    select_accountname_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr[2]/td[1]/a")
    #查询到的账户创建日期
    select_accounttime_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr[2]/td[2]")
    #查询到的账户已检测篇数
    select_accountchecked_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr[2]/td[2]")
    #查询到的账户剩余篇数
    select_accountchect_loc=(By.ID,".//*[@id='1_td']")
    #查询列表
    selectaccount_list_loc=(By.XPATH,"html/body/div[4]/div[3]/table/tbody/tr")



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
    cancel_modifyCount_loc=(By.XPATH,".//*[@id='dialog-updateCheckCount']/button")
    #分配失败提示
    checkCount_fail_loc=(By.ID,"validateTips-updateCheckCount")
    #现在的篇数
    now_checkCount_loc=(By.ID,"2_td")
    #操作-修改密码
    operation_updatePassword_loc=(By.ID,"2_updatePassword")
    #新密码
    newPassword_loc=(By.ID,"newPassword")
    #确认新密码
    renewPassword_loc=(By.ID,"renewPassword")
    #确定修改密码
    confirm_updatePassword_loc=(By.ID,"confirmUpdatePasswordBtn")
    #修改密码提示
    updatePassword_remind_loc=(By.ID,"validateTips-updatePassword")
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
        self.find_element(*self.createUser_button_loc).click()

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

    def create_newAccountName(self):
        '''新创建的子账户名称'''
        return self.find_element(*self.newAccount_name_loc).text
    def createAccount_error_remind(self):
        '''创建子账户错误提示'''
        return self.find_element(*self.createError_remind_loc).text
    def checkquritity_remind(self):
        '''可分配篇数提示'''
        return self.find_element(*self.checkQuantity_remind_loc).text

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
    def select_success_remind(self):
        return self.find_element(*self.userName_link_loc).text


    def export_button(self):
        '''导出按钮'''
        self.find_element(*self.export_button_loc).click()

    #判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName(self):
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        if os.listdir(dir_path):
            os.rename(dir_path+"\账户管理统计表.xls",dir_path+r"\%s.xls"%(name))
            # os.rename(r"E:\PyCharm_Workspace\simily_shuobo\testData\downloadFiles\子账户列表导出.xls",r"E:\PyCharm_Workspace\simily_shuobo\testData\downloadFiles\%s.xls"%(name))
            #print("文件夹不为空")
        else:
            pass

    def verifyExist(self):
        #判断是否下载到本地,返回bool类型的True或False
        #判断文件是否存在
        dir_path=GetPath().getAbsoluteDirPath("downloadFiles")
        flag = os.path.exists(dir_path+"\账户管理统计表.xls")
        return flag

    def operation_checkQuantity_button(self):
        '''分配篇数按钮'''
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
    def checkCount_fail_remind(self):
        '''分配成功提示'''
        return self.find_element(*self.checkCount_fail_loc).text
    def now_checkCount(self):
        '''当前剩余篇数'''
        #return self.find_element(*self.now_checkCount_loc).text
        text=self.find_element(*self.now_checkCount_loc).text
        nowCount=int(text)
        return nowCount



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
    def modifyPassword_remind(self):
        return self.find_element(*self.updatePassword_remind_loc).text



    def account_link(self):
        '''账户链接'''
        self.find_element(*self.userName_link_loc).click()
    def informationManage_title(self):
        '''信息管理页面标题'''
        return self.find_element(*self.informationManage_title_loc).text


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
        return self.find_element(*self.operation_lock_loc).text

    def list_search(self,accountname):
        '''
        按照任务名称查询
        :param task_name:任务名称
        :return:返回状态用来判断查询结果
        '''
        '''输入查询账户'''
        self.find_element(*self.select_UserName_loc).clear()
        self.find_element(*self.select_UserName_loc).send_keys(accountname)
        self.find_element(*self.select_button_loc).click()
        time.sleep(2)

        list_num=len(self.find_elements(*self.selectaccount_list_loc))
        #print(list_num)
        i=2
        for num in range(1,list_num):
            try:
                #print(i)
                text=self.driver.find_element_by_xpath("html/body/div[4]/div[3]/table/tbody/tr[%s]/td[1]/a" % i).text
                print(text)
                if accountname in text:
                    if i==list_num+1:
                        return True
                    i=i+1
                else:
                    print("账户名称查询问题")
            except Exception as msg:
                print(msg)










