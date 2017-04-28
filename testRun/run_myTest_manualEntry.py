#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:51
# @Author  : Nxy
# @Site    : 
# @File    : run_manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox

class RunManualEntry(myUnitChrome.UnitChrome):
    def test_selectExistingTasks_run(self):
        pass
    def test_addContent_run(self):
        pass
    def test_startTest_run(self):
        pass
    def test_viewTestResults_run(self):
        pass
