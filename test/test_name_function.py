#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\test\test_name_function.py
# Project: c:\Users\jlei1\PyTestProj\test
# Created Date: Tuesday, December 3rd 2019, 1:31:23 pm
# Author: Ji Lei
# -----
# Last Modified: Sat Jun 20 2020
# Modified By: Ji Lei
# -----
# Copyright (c) 2019 eBay
# 
# eBay internal ONLY. Any copy and change besides Ji Lei will be seen as invalid.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
# 2019-12-03	JL	initial version, change vscode launch.json cwd to {currentWorkingFolder}
#####################################################################################

import sys
if not ('../' in sys.path):
    sys.path.insert(0,'../')

import unittest
from PyTestProj.name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test name_function.py, the test functions must start with tes_
       with this, unittest will test these function automatically
    """

    def test_first_last_name(self):
        """can the name_function.py handle name like 'Janis Joplin'?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """can the name_function.py handle name like 'Martin Luther King'?"""
        formatted_name = get_formatted_name('martin', 'king', 'luther')
        self.assertEqual(formatted_name, 'Martin Luther King')

unittest.main()

