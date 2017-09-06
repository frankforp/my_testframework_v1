#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 3:28 PM
# @Author  : Winnichen
# @File    : test_case1.py
from config import settings
import logging
from pages.mypage import MyPage
from utils.public import public
import time
def test_add():
    dr=public().get_driver()
    tp=MyPage(dr,settings.url,"百度一下，你就知道")
    tp.open_wait()
    tp.input_content("python")
    tp.click_search()
    time.sleep(3)
    dr.quit()