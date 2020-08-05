#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\test\test_city_function.py
# Project: c:\Users\jlei1\PyTestProj\test
# Created Date: Tuesday, December 3rd 2019, 2:36:57 pm
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
# 2019-12-03	JL	Practice for test city function
#####################################################################################

import sys
if not ('../' in sys.path):
    sys.path.insert(0,'../')

import unittest
from PyTestProj.city_function import format_location

class CityTestCase(unittest.TestCase):
    """test city_function.py
    """

    def test_city_country(self):
        """test for handling 'santiago', 'chile'
        """
        formatted_location = format_location('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        """test for handing 'santiago', 'chile', 'population=500000'
        """
        formatted_location = format_location('santiago','chile',500000)
        self.assertEqual(formatted_location,'Santiago, Chile - population 500000')

unittest.main()