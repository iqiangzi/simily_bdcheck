#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_batchDetection.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunBatchDetection(myUnitChrome.UnitChrome):
    def test_selectExistingTasks_run(self):
        pass
    def test_addPaper_run(self):
        pass
    def test_startUpload_run(self):
        pass
    def test_continueAdd_run(self):
        pass
    def test_deletePaper_run(self):
        pass
    def test_startTest_run(self):
        pass
    def test_viewTestResults_run(self):
        pass
