#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\name_function.py
# Project: c:\Users\jlei1\PyTestProj
# Created Date: Tuesday, December 3rd 2019, 1:19:23 pm
# Author: Ji Lei
# -----
# Last Modified: Tue Dec 03 2019
# Modified By: Ji Lei
# -----
# Copyright (c) 2019 eBay
# 
# eBay internal ONLY. Any copy and change besides Ji Lei will be seen as invalid.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
#####################################################################################

def get_formatted_name(first, last, middle=''):
    """ Generate a neatly formatted full name
    """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

