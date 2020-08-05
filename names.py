#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\names.py
# Project: c:\Users\jlei1\PyTestProj
# Created Date: Tuesday, December 3rd 2019, 1:22:14 pm
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


from name_function import get_formatted_name

print("Enter 'q' to quit at any time.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
