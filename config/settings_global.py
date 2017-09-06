#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 3:28 PM
# @Author  : Winnichen
# @File    : settings_global.py
import pytest
testcase_path="./autocase/testCase.xlsx"
browser=pytest.config.getoption('--browser').lower()
if browser not in ("chrome","ie","firefox"):
    browser="chrome"