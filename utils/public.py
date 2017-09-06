#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/16/2017 10:56 AM
# @Author  : Winnichen
# @File    : public.py
from selenium import webdriver
import logging,time,os
from config import settings

class public(object):
    def get_driver(self):
        browser=settings.browser.lower()
        if(browser=="chrome"):
            dr=webdriver.Chrome()
        elif(browser=="ie"):
            dr=webdriver.Ie()
        elif(browser=="firefox"):
            dr=webdriver.Firefox()
        else:
            logging.error("Wrong browser")
            assert 0
        dr.maximize_window()
        return dr

    def take_screenshot(self,dr,info):
        if not os.path.isdir("screenshots"):
            os.mkdir("screenshots")
        fmt='-%Y%m%d%H%M%S'
        Date=time.strftime(fmt,time.localtime(time.time()))
        picname=config.screenshot_path+info+Date+".jpg"
        dr.get_screenshot_as_file(picname)