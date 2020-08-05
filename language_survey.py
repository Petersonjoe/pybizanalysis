#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\language_survey.py
# Project: c:\Users\jlei1\PyTestProj
# Created Date: Tuesday, December 3rd 2019, 5:00:39 pm
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


from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while  True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

