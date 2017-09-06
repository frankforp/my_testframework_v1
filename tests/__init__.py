#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/23/2017 3:28 PM
# @Author  : Winnichen
# @File    : __init__.py.py
import os
if not os.path.isdir("logs"):
    os.mkdir("logs")
import utils.log_writer
