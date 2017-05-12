#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : taskList.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
import time
from time import sleep
from selenium.webdriver.support.ui import Select
from util.toolUtils.getPath import GetPath
import os

class TaskList(BasePage):
    # 定位
    # 任务名称
    task_name_loc = (By.ID,"taskNameInput")
    # 日期控件-4月
    time_month_loc = (By.XPATH,".//*[@id='ui-datepicker-div']/div/div/select[2]/option[4]")
    # 时间-4月1日
    time_day_loc = (By.XPATH,".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[6]/a")
    # 查询按钮
    search_button_loc = (By.XPATH,".//*[@id='searchTaskForm']/div/input")
    # 任务名称列表：总结出查询结果中的任务数目
    task_list_loc = (By.XPATH, "html/body/div[4]/div[3]/table/tbody/tr/td[2]")
    author_link_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr")
    # 分页定位
    paging_select_loc = (By.ID, "sel")
    # 首页，上一页
    home_pageBtn_loc = (By.XPATH,"html/body/div[4]/div[3]/form[2]/p/a[1]")
    up_pageBtn_loc = (By.XPATH,"html/body/div[4]/div[3]/form[2]/p/a[2]")
    # 跳转到第3页
    three_Btn_loc=(By.XPATH,"html/body/div[4]/div[3]/form[2]/p/a[3]")
    # 下一页，末页
    next_pageBtn_loc = (By.XPATH, "html/body/div[4]/div[3]/form[2]/p/a[10]")
    last_pageBtn_loc = (By.XPATH, "html/body/div[4]/div[3]/form[2]/p/a[9]")
    # 页面显示信息：当前是第几页
    now_pageNum_loc = (By.XPATH, "html/body/div[4]/div[3]/form[2]/p/span[4]")
    # 第一行的检测状态
    test_status_loc = (By.XPATH, "html/body/div[4]/div[3]/table/tbody/tr[2]/td[5]")
    # 操作显示
    op_display_loc = (By.XPATH, "html/body/div[4]/div[3]/table/tbody/tr[2]/td[6]/a")
    # 任务名称链接
    taskName_Link_loc = (By.XPATH, "html/body/div[4]/div[3]/table/tbody/tr[2]/td[2]/a")
    task_nameIn_loc = (By.XPATH, ".//*[@id='searchTaskItemForm']/div[1]/b")
    # 上传按钮 元素
    up_btn_loc = (By.XPATH, "//div[@class='colleTaskbtn']/div/div[1]")
    # 开始检测按钮 元素
    test_btn_loc = (By.ID, "beginCheck")
    # 相似比
    similarR_start_loc=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[1]/span[1]/input")
    similarR_end_loc=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[1]/span[3]/input")
    # 篇名
    title_input_loc=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[1]/input[1]")
    # 作者
    author_input_loc=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[1]/input[2]")
    # 查询按钮
    search_btn_loc=(By.XPATH, ".//*[@class='blueBtnsmal']")
    # 第一行的篇名，作者，相似比
    firstL_title_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[4]/a")
    firstL_author_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[5]/a")
    firstL_similar_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[8]")
    # 进入后的查询
    task_search_loc = (By.XPATH, ".//*[@id='searchTaskItemForm']/div[2]/p[2]/input")
    #选择状态
    #select_status_choose = (By.XPATH,".//*[@id='searchTaskItemForm']/div[2]/p[2]/select")
    task_result_status = (By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[7]")
    # 下载报告 按钮
    down_report_btn = (By.ID, "downLoadReport")
    # 勾选复选框
    select_btn=(By.ID, "allchecked")
    # 转移按钮
    transfor_btn_loc=(By.ID, "moveToOtherTask")
    # 第一个任务
    first_task_loc=(By.XPATH, ".//*[@id='moveToOtherTaskList']/li[1]")
    # 第一行复选框
    first_select_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[2]/input")
    # 标记为按钮
    mark_btn_loc=(By.ID, "markPaper")
    # 标记为问题论文
    mark_problem_btn=(By.ID, "markTroublePaperBtn")
    # 取消标记为问题论文
    concel_mark_paper=(By.ID, "unMarkTroublePaperBtn")
    # 问题论文 数目
    mark_problem_num=(By.XPATH, ".//*[@id='searchTaskItemForm']/div[1]/span/span[2]")
    # 检测时间控件
    test_time_order=(By.ID, "dateSortBy")
    # V2.0相似比排序控件
    similar_radio_order=(By.XPATH, ".//*[@id='copyprecentSortBy'][2]")
    # V1.0相似比排序控件
    similar_radio_order1=(By.XPATH, ".//*[@id='copyprecentSortBy'][1]")
    # 简明报告
    report1_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/label[1]")
    # 详细报告
    report2_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/label[2]")
    # 全文报告
    report3_loc=(By.XPATH, "html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/label[3]")
    # 在线报告
    mark_loc=(By.ID, "Simple")
#------------------------------------------------------------------------------------------------------------------
    def list_search(self,task_name):
        '''
        按照任务名称查询
        :param task_name:任务名称
        :return:返回状态用来判断查询结果
        '''
        self.find_element(*self.task_name_loc).send_keys(task_name)
        self.find_element(*self.search_button_loc).click()
        list_num=len(self.find_elements(*self.task_list_loc))
        # print(list_num)
        i=2
        for num in range(1,list_num+1):
            try:
                # print(i)
                text=self.driver.find_element_by_xpath("html/body/div[4]/div[3]/table/tbody/tr[%s]/td[2]/a" % i).text
                # print("text",text)
                if task_name in text:
                    if i==list_num+1:
                        return True
                    i=i+1
                else:
                    print("任务名称查询问题")
            except Exception as msg:
                print(msg)
    def time_search(self,month1,row1,column1,month2,row2,column2):
        '''
        选择时间日期查询
        :param month1:开始日期中的月份
        :param raw1:开始日期中的日所在的行
        :param column1:开始日期中的日所在的列
        :param month2:结束日期中的月份
        :param row2:结束日期中的日所在的行
        :param column2:结束日期中的日所在的列
        :return:
        '''
        self.driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        # 下拉框 点击
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month1).click()
        # 选择日
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row1,column1)).click()
        # 点击选择结束日期
        self.driver.find_element_by_xpath("(//img[@alt='...'])[2]").click()
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month2).click()
        #self.find_element(*self.time_month_loc).click()
        # 选择日
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row2,column2)).click()
        # 点击查询按钮
        self.find_element(*self.search_button_loc).click()
        # 定位第一行日期
        text=self.driver.find_element_by_xpath("html/body/div[4]/div[3]/table/tbody/tr[2]/td[3]").text
        return text
    def pageChoose(self, record_num):
        '''
        选择每页显示条数
        :param record_num: 1,2,3 对应选择10 20 50
        :return: 返回第一页条数和选择的每页显示数字
        '''
        self.find_element(*self.paging_select_loc).click()
        self.driver.find_element_by_xpath(".//*[@id='sel']/option[%s]" % record_num).click()
        list_num=len(self.find_elements(*self.task_list_loc))
        # len() return 'int'
        #list_n=str(list_num)
        # 定位中不能打印出text
        # now_num=self.find_element(*self.paging_select_loc).text
        return list_num
    def pageNum(self):
        now_page=self.find_element(*self.now_pageNum_loc).text
        now_pageNum=now_page[1:now_page.index('/')]
        return now_pageNum
    def pageSkip(self,num):
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/form[2]/p/a[%s]" % num).click()
    def statusOp(self):
        test_status=self.find_element(*self.test_status_loc).text
        op_display=self.find_element(*self.op_display_loc).text
        if test_status=="等待添加论文":
            if op_display=="添加论文":
                return True
        elif test_status=="暂停检测":
            if op_display=="继续检测":
                return True
        elif test_status=="检测完成":
            if op_display=="":
                return True

    def taskNameLink(self,taskName):
        self.find_element(*self.task_name_loc).send_keys(taskName)
        self.find_element(*self.search_button_loc).click()
        time.sleep(2)
        task_name = self.find_element(*self.taskName_Link_loc).text
        self.find_element(*self.taskName_Link_loc).click()
        sleep(1)
        task_name_in = self.find_element(*self.task_nameIn_loc).text
        return task_name,task_name_in
    def operationLink(self):
        try:
            op_name = self.find_element(*self.op_display_loc).text
            # 进入链接
            self.find_element(*self.op_display_loc).click()
            # sleep(2)
            if op_name == "添加论文":
                flag=self.is_element_visible(self.up_btn_loc)
                return flag
            elif op_name == "继续检测":
                flag=self.is_element_visible(self.test_btn_loc)
                return flag
        except Exception:
            flag = True
            return flag
    def similarSearch(self, startR, endR, title, author):
        '''
        :param startR:相似比初始
        :param endR:相似比结束
        :param title:篇名
        :param author:作者
        :return:
        '''
        self.find_element(*self.similarR_start_loc).send_keys(startR)
        self.find_element(*self.similarR_end_loc).send_keys(endR)
        self.find_element(*self.title_input_loc).send_keys(title)
        self.find_element(*self.author_input_loc).send_keys(author)
        self.find_element(*self.search_btn_loc).click()
        sleep(1)
        lineT=self.find_element(*self.firstL_title_loc).text
        lineA=self.find_element(*self.firstL_author_loc).text
        # string类型转化为 float类型
        str = self.find_element(*self.firstL_similar_loc).text
        str1 = str.split("|")
        lineS=float(str1[0])
        # print(lineS)
        if (title in lineT) and (author in lineA):
            if (lineS >= float(startR)) and (lineS <= float(endR)):
                return  True

    def timeStatusSearch(self,month1,row1,column1,month2,row2,column2,status):
        '''
        选择时间日期查询
        :param month1:开始日期中的月份
        :param raw1:开始日期中的日所在的行
        :param column1:开始日期中的日所在的列
        :param month2:结束日期中的月份
        :param row2:结束日期中的日所在的行
        :param column2:结束日期中的日所在的列
        :return:
        '''
        self.driver.find_element_by_css_selector("img.ui-datepicker-trigger").click()
        # 下拉框 点击
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 选择月份 5
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month1).click()
        # 选择日 1 5
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row1,column1)).click()
        # 点击选择结束日期
        self.driver.find_element_by_xpath("(//img[@alt='...'])[2]").click()
        self.driver.find_element_by_css_selector("select.ui-datepicker-month").click()
        # 选择月份
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]/option[%s]" % month2).click()
        #self.find_element(*self.time_month_loc).click()
        # 选择日 1 5
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[%s]/td[%s]/a" % (row2,column2)).click()
        # 选择状态
        # self.find_element(*self.select_status_choose).click()
        # 选择检测成功
        # self.driver.find_element_by_xpath(".//*[@id='searchTaskItemForm']/div[2]/p[2]/select/option[%s]" % i).click()
        Select(self.driver.find_element_by_name("State")).select_by_visible_text(status)# 点击查询按钮
        self.find_element(*self.task_search_loc).click()
        sleep(1)
        # 定位第一行日期 html/body/div[4]/div[2]/table/tbody/tr[2]/td[6]
        date=self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[6]").text
        # 定位 状态 test_status_loc
        str=self.find_element(*self.task_result_status).text
        status_str= str.split("｜")
        result_status = status_str[0]
        # return date,status
        if result_status == status:
            return date

    # 点击下载报告 按钮
    def downloadReport(self):
        self.find_element(*self.select_btn).click()
        self.find_element(*self.down_report_btn).click()
        #pass

    # 判断目录中是否存在同名文件 有的话返回True
    def downVerify(self):
        ab_path = GetPath().getAbsoluteFilePath("ncy(V1.0简明版报告).zip",r"downloadFiles\ncy(V1.0简明版报告).zip")
        flag = os.path.exists(ab_path)
        return flag

    #判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName(self):
        ab_path = GetPath().getAbsoluteFilePath("ncy(V1.0简明版报告).zip",r"downloadFiles\ncy(V1.0简明版报告).zip")
        ab_path_rename = GetPath().getAbsoluteFilePath("ncy(V1.0简明版报告).zip",r"downloadFiles")
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        if os.path.exists(ab_path):
            os.rename(ab_path,ab_path_rename+"\%s.zip"%(name))
            print("文件夹不为空")
        else:
            #pass
            print("文件夹为空")

    # 输入篇名，点击搜索
    def title_search(self,title):
        self.find_element(*self.title_input_loc).send_keys(title)
        self.find_element(*self.search_btn_loc).click()
    # 转移任务
    def transferTask(self):
        # 点击 下拉框
        self.find_element(*self.transfor_btn_loc).click()
        # 选择第一个项目
        self.find_element(*self.first_task_loc).click()
        time.sleep(2)
    # 搜索之后第一个行的人物名
    def taskName(self):
        task = self.find_element(*self.first_task_loc).text
        return task

    #返回任务列表
    def returnTask(self,task,verify_title):
        # 点击 我的检测
        self.driver.find_element_by_xpath(".//*[@id='searchTaskItemForm']/div[1]/a").click()
        # 任务名称 检索
        self.find_element(*self.task_name_loc).send_keys(task)
        self.find_element(*self.search_button_loc).click()
        time.sleep(1)
        # 进入名称链接
        self.find_element(*self.taskName_Link_loc).click()
        time.sleep(1)
        # 输入篇名
        self.find_element(*self.title_input_loc).send_keys(verify_title)
        # 点击查询按钮
        self.find_element(*self.search_btn_loc).click()
        sleep(1)
        title=self.find_element(*self.firstL_title_loc).text
        return title
    # 标记为问题论文
    def markProblem(self):
        # self.find_element(*self.first_select_loc).click()
        self.find_element(*self.mark_btn_loc).click()
        self.find_element(*self.mark_problem_btn).click()
        time.sleep(1)
    # 取消标记为问题论文
    def concelMark(self):
        self.find_element(*self.mark_btn_loc).click()
        self.find_element(*self.concel_mark_paper).click()
    # 显示问题论文的数目
    def paperNum(self):
        problem_num=self.find_element(*self.mark_problem_num).text
        return problem_num
        # pass
    def paperNameLink(self):
        title = self.find_element(*self.firstL_title_loc).text
        author = self.find_element(*self.firstL_author_loc).text
        newTitle = title+'+'+author+'.pdf'
        self.find_element(*self.firstL_title_loc).click()
        return newTitle

    # 判断目录中是否存在同名文件 有的话返回True
    def downVerify1(self,newTitle):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        flag = os.path.exists(ab_path)
        return flag

    # 判断文件夹是否为空，不为空则重命名同名文件，以保证新下载的文件的唯一性。为空则直接下载
    def renameFileName1(self,newTitle):
        ab_path = GetPath().getAbsoluteFilePath(newTitle,r"downloadFiles\%s" % newTitle)
        ab_path_rename = GetPath().getAbsoluteFilePath("%s" % newTitle,r"downloadFiles")
        #获取当前时间
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        if os.path.exists(ab_path):
            os.rename(ab_path,ab_path_rename+"\%s.pdf"%(name))
            print("文件夹不为空")
        else:
            #pass
            print("文件夹为空")

    def authorLink(self):
        # 点击第一行的作者
        self.find_element(*self.firstL_author_loc).click()
        auther_name = self.find_element(*self.firstL_author_loc).text
        list_num=len(self.find_elements(*self.author_link_loc))
        #print(list_num)
        i=2
        for num in range(1,list_num):
            try:
                #print(i)
                auther=self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[%s]/td[5]/a" % i).text
                #print("text",auther)
                #print(auther_name)
                if auther_name == auther:
                    print("有")
                    if i==list_num:
                        return True
                    i=i+1
                else:
                    print("查询问题")
            except Exception as msg:
                print(msg)
    def viewOnlineReports(self):
        pass

    # 层层返回
    def alert(self):
        return super(TaskList,self).confirm_broserAlert()

    def timeOrder(self):
        date1 =self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[6]").text
        new_time = time.strptime(date1,"%Y-%m-%d %H:%M")
        self.find_element(*self.test_time_order).click()
        date2 = self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[6]").text
        old_time = time.strptime(date2,"%Y-%m-%d %H:%M")
        if new_time >= old_time:
            return True
    # 对应V1.0
    def similarOrder(self):
        self.find_element(*self.similar_radio_order).click()
        str = self.find_element(*self.firstL_similar_loc).text
        a=str.split("|")
        # 1对应1.0
        one_similar = float(a[1])
        print(one_similar)
        self.find_element(*self.similar_radio_order).click()
        str2 = self.find_element(*self.firstL_similar_loc).text
        b = str2.split("|")
        two_similar = float(b[1])
        print(two_similar)
        if one_similar >= two_similar:
            return True

    # 对应V2.0
    def similarOrder1(self):
        self.find_element(*self.similar_radio_order1).click()
        str = self.find_element(*self.firstL_similar_loc).text
        a=str.split("|")
        # 1对应1.0
        one_similar = float(a[0])
        # print(one_similar)
        self.find_element(*self.similar_radio_order1).click()
        str2 = self.find_element(*self.firstL_similar_loc).text
        b = str2.split("|")
        two_similar = float(b[0])
        # print(two_similar)
        if one_similar >= two_similar:
            return True

    # 下载报告 1 2 3 对应 简明报告 详细报告 全文报告
    def downReport(self,label_num):
        return self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[9]/label[%s]" % label_num).text

    def loadReport(self):
        title = self.find_element(*self.firstL_title_loc).text
        author = self.find_element(*self.firstL_author_loc).text
        newTitle = title+'+'+author
        return newTitle

    def loadReport1(self):
        title = self.find_element(*self.firstL_title_loc).text
        newTitle ='《'+ title+'》 '
        return newTitle

    def onlineReport(self,num):
        # 转换句柄
        now_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath("html/body/div[4]/div[2]/table/tbody/tr[2]/td[10]/a[%s]" % num).click()
        # 获取所有的句柄
        all_handles=self.driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to.window(handle)
                flag = self.is_element_visible(self.mark_loc)
                return flag










