#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:52
# @Author  : Ncy
# @Site    :
# @File    : studentAccount.py
# @Software: PyCharm
from selenium import  webdriver

from testCase.pageObj.basePage import BasePage
import time
from time import sleep
from selenium.webdriver.common.by import By
import os
from util.toolUtils.getPath import GetPath

class StuAccountList(BasePage):
    #search_btn_loc=(By.ID, "searchBtn")
    #搜索列表的定位
    first_line_time = (By.XPATH, ".//*[@id='container']/table/tbody/tr[2]/td[3]")
    # 批次搜索框
    batch_input_loc = (By.ID, "batchInfoOld")
    # 批次名称
    batch_name_loc = (By.XPATH, ".//*[@id='container']/table/tbody/tr[2]/td[2]")
    # 学生列表：总结出查询结果中的任务数目
    task_list_loc = (By.XPATH, ".//*[@id='container']/table/tbody/tr/td[2]")
    # 分页定位
    paging_select_loc = (By.ID, "sel")
    # 首页，上一页
    home_pageBtn_loc = (By.XPATH,".//*[@id='container']/div/form/p/a[1]")
    up_pageBtn_loc = (By.XPATH,".//*[@id='container']/div/form/p/a[2]")
    # 跳转到第3页
    three_Btn_loc=(By.XPATH,".//*[@id='container']/div/form/p/a[3]")
    # 下一页，末页
    next_pageBtn_loc = (By.XPATH, ".//*[@id='container']/div/form/p/a[8]")
    last_pageBtn_loc = (By.XPATH, ".//*[@id='container']/div/form/p/a[9]")
    # 页面显示信息：当前是第几页
    now_pageNum_loc = (By.XPATH, ".//*[@id='container']/div/form/p/span[4]")
    # 上面显示批次信息
    display_msg_loc = (By.XPATH, "html/body/div[4]/div[3]/div[1]/span[2]")
    # 批次
    batch_loc=(By.XPATH, ".//*[@id='select-box']/input[1]")
    # 学生账户
    studentAccount_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/div[2]/input[1]")
    # 相似比
    similar_radio1_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/span[2]/input")
    similar_radio2_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/span[3]/input")
    # 检测次数
    test_num1_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/input[1]")
    test_num2_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/input[2]")
    # 学生账户
    student_account_input=(By.XPATH,"html/body/div[4]/div[3]/form[1]/div/div[2]/input[1]")
    # 查询按钮
    search_btn_loc=(By.XPATH, "html/body/div[4]/div[3]/form[1]/div/div[2]/input[2]")
    # 第一行的信息
    first_line_account=(By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[2]")
    first_similar_radio=(By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[4]")
    first_batch_loc=(By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[7]")
    first_test_num=(By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[5]")
    # 学生账户详情
    # 子账户
    fist_sub_account = (By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[2]/a")
    # 个人检测详情
    account_detail = (By.XPATH, "html/body/div[4]/div[2]/div[2]/p[1]")
    # 个人检测为空时text
    text_loc = (By.XPATH, "html/body/div[4]/div[2]/p")
    # 有效期显示
    time_display_loc=(By.XPATH, ".//*[@id='container']/tbody/tr[2]/td[9]/span/label")

#-----------------------------------------------------------------------------------
    def timeSearch(self, month1, row1,column1,month2, row2, column2):
        '''
        :param month1,month2:选择的月
        :param row1,column1:起始日期的日的坐标
        :param row2,column2:结束日期的日的坐标
        :return:
        '''
        self.driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 选择4月 对应4
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month1).click()
        # 1,6对应4月的1日
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row1,column1)).click()
        self.driver.find_element_by_xpath("(//img[@alt='...'])[2]").click()
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 结束日期对应的时间 1对应4
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month2).click()
        # 5,5对应4月的28日
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row2,column2)).click()

    def firstTime(self):
        first_time = self.find_element(*self.first_line_time).text
        return first_time
    def batchSearch(self,batch_name):
        self.find_element(*self.batch_input_loc).send_keys(batch_name)
    def firstBatch(self):
        batch = self.find_element(*self.batch_name_loc).text
        return batch

    # 分页部分
    def pageChoose(self, record_num):
        '''
        选择每页显示条数
        :param record_num: 1,2,3 对应选择10 20 50
        :return: 返回第一页条数和选择的每页显示数字
        '''
        self.find_element(*self.paging_select_loc).click()
        self.driver.find_element_by_xpath(".//*[@id='sel']/option[%s]" % record_num).click()
        time.sleep(1)
        list_num=len(self.find_elements(*self.task_list_loc))
        return list_num
    def pageNum(self):
        now_page=self.find_element(*self.now_pageNum_loc).text
        now_pageNum=now_page[1:now_page.index('/')]
        return now_pageNum
    def pageSkip(self,num):
        self.driver.find_element_by_xpath(".//*[@id='container']/div/form/p/a[%s]" % num).click()

    # 判断目录中是否存在同名文件 有的话返回True
    def downVerify1(self,newTitle):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        flag = os.path.exists(ab_path)
        return flag

    # 判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName1(self,newTitle,suffix):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        ab_path_rename = GetPath().getAbsoluteFilePath("%s" % newTitle,r"downloadFiles")
        #获取当前时间
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        if os.path.exists(ab_path):
            os.rename(ab_path,ab_path_rename+"\%s%s"%(name,suffix))
            print("文件夹不为空")
        else:
            #pass
            print("文件夹为空")

    # 打印显示信息
    def displayMsg(self):
        return self.find_element(*self.display_msg_loc).text
    # 选择批次和输入学生账户
    def batchAccount(self,item,stuAccount):
        # 选择批次
        self.find_element(*self.batch_loc).click()
        self.driver.find_element_by_xpath(".//*[@id='select-box']/ul/li[%s]" % item).click()
        self.find_element(*self.student_account_input).send_keys(stuAccount)
    # 点击查询按钮
    def searchBtn(self):
        self.find_element(*self.search_btn_loc).click()
    # 返回批次和账号信息
    def batchMsg(self):
        batch = self.find_element(*self.first_line_account).text
        account = self.find_element(*self.first_batch_loc).text
        return batch,account
    # 选择相似比和检测次数
    def similarTest(self,radio1,radio2,test1,test2):
        self.find_element(*self.similar_radio1_loc).send_keys(radio1)
        self.find_element(*self.similar_radio2_loc).send_keys(radio2)
        self.find_element(*self.test_num1_loc).send_keys(test1)
        self.find_element(*self.test_num2_loc).send_keys(test2)
    # 返回相似比和篇数
    def similarMsg(self,radio1,radio2, test1,test2):
        list_len=len(self.driver.find_elements_by_xpath(".//*[@id='container']/tbody/tr"))
        print(list_len)
        i = 2
        for num in range(1,list_len):
            print(i)
            # 从2开始 str 相似比
            str=self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[%s]/td[4]" % i).text
            str1 = str.split("｜")
            radio = str1[0]
            # print(radio)
            # 对应 检测次数
            test_num=self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[5]").text
            print(test_num)
            if radio >= radio1 and radio <=radio2:
                if test_num >= test1 and test_num <= test2:
                    if i == list_len:
                        # print("Ok")
                        return True
            i += 1

    # 学生账户详情中 - 学生账号链接
    def accountLink(self):
        sub_account = self.find_element(*self.fist_sub_account).text
        # print(sub_account)
        self.find_element(*self.fist_sub_account).click()
        time.sleep(1)
        perAccount = self.find_element(*self.account_detail).text
        perAccount1= perAccount.split("：")
        personalAccount=perAccount1[1]
        # print(personalAccount)
        if sub_account == personalAccount:
            return True

    def personalTest(self):
        # 对应 检测次数
        test_num=self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[5]").text
        # print(test_num)
        # 点击第一个账号链接
        self.accountLink()
        if test_num == "0":
            msg = self.find_element(*self.text_loc).text
            return msg
        else:
            flag = self.is_element_visible(self.text_loc)
            return flag

    def optionBtn(self,btn_name,i):
        '''
        :param btn_name:按钮名称
        :param i:对应第几行
        '''
        a="(//a[contains(text(),'%s')])[%s]" % (btn_name,i)
        # print(a)
        self.driver.find_element_by_xpath(a).click()
        # print("更改有效期")
    # 选择时间
    def optionTime(self,i,row,column):
        # 单击日期控件
        self.driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]").click()
        # 2 现在当前时间是2017/5 2对应6月
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % i).click()
        # 选择日期1 4 对应6月1号
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" %(row,column)).click()
        time.sleep(2)
        # 点击确定按钮
        self.driver.find_element_by_link_text("确定").click()
        time.sleep(1)
        return self.find_element(*self.time_display_loc).text
    #增加篇数
    def addArticle(self,article_num):
        time.sleep(1)
        self.driver.find_element_by_id("districount").send_keys(article_num)
        self.driver.find_element_by_id("distributeOK").click()
        time.sleep(1)

    #转移批次
    def transferBatch(self,i):
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='editBatch']/p[2]/select").click()
        # 2对应批次lytest111
        self.driver.find_element_by_xpath(".//*[@id='editBatch']/p[2]/select/option[%s]" % i).click()
        # 点击确定按钮
        self.driver.find_element_by_id("editBatchOK").click()
        time.sleep(1)
    # 点击名称链接
    def personalPaper(self,row):
        paper = self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[%s]/td[1]/a" % row).text
        return paper
    # 下载报告
    def personalDown(self,row):
        # 详细报告 对应1 全文报告对应2
        str = self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[6]/label[%s]" % row).text
        detail_str = str[:2]
        return detail_str
    def versionLink(self,row1,row2):
        # 6,1 对应详细报告V2.0
        self.driver.find_element_by_xpath(".//*[@id='container']/tbody/tr[2]/td[%s]/a[%s]" % (row1,row2)).click()