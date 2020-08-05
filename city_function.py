#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\city_function.py
# Project: c:\Users\jlei1\PyTestProj
# Created Date: Tuesday, December 3rd 2019, 2:33:59 pm
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
# 2019-12-03	JL	a presudo test for city function
#####################################################################################

def format_location(city, country, population=None):
    formatted_location = city + ', ' + country
    if population:
        return formatted_location.title() + ' - population ' + str(population)
    else:
        return formatted_location.title()
