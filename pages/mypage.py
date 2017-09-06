#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 4:52 PM
# @Author  : Winnichen
# @File    : mypage.py
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
import os,time

class MyPage(BasePage):
    search_loc=(By.ID,"kw")
    button_loc=(By.ID,"su")

    def input_content(self,content):
        logging.info("input...................")
        self.send_keys(self.search_loc,content)

    def click_search(self):
        self.find_element(*self.button_loc).click()