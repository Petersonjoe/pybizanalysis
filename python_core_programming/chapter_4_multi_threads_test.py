#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################################
# File: c:\Users\jlei1\PyTestProj\multi_threads.py
# Project: c:\Users\jlei1\PyTestProj
# Created Date: Friday, December 27th 2019, 3:59:53 pm
# Author: Ji Lei
# -----
# Last Modified: Fri Dec 27 2019
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


# python 多线程编程包含编译器自带的 threading 模块，其中的thread类用以创建多线程实例
# 有多种方式来设计多线程程序
# 1. 创建一个thread多线程实例，并传递一个函数给该实例
# 2. 创建一个thread多线程实例，并传递一个“可调用”的类实例
# 3. 派生一个thread的子类，并创建子类的实例

# 以下就3种不同的使用方式加以应用
import threading
from time import sleep, ctime

def loop(nloop, nsec):
    print('start loop ', nloop, ' at: ',ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at: ',ctime())

#---------- 1. 创建一个thread多线程实例，并传递一个函数给该实例 ----------#
# loops = [4,2]

# def main():
#     print('start at: ', ctime())
#     threads = []
#     nloops = range(len(loops))

#     for i in nloops:
#         # 开始创建thread实例，这里Thread()中直接再run()方法中调用args传入的参数供target传入的函数使用
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
    
#     # 启动各个线程
#     for i in nloops:
#         threads[i].start()

#     # 等待所有线程结束， join(timeout=None) 直至启动的线程终止之前一直挂起，除非给出timeout（sec），否则一直阻塞
#     for i in nloops:
#         threads[i].join()

#     print('all DONE at: ', ctime())

# if __name__ == "__main__":
#     main()


#---------- 2. 创建一个thread多线程实例，并传递一个“可调用”的类实例 ----------#
loops = [4,2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
    
    # 这里重写了__call__方法，类实例的调用就可以直接用__call__()的参数列表顺序
    # 用*args的方式，则func按照默认顺序输入的参数列表
    def __call__(self):
        self.func(*self.args)

def main():
    print('start at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # ThreadFunc()直接调用而不是先产生一个实例主要是因为__call__()方法的特性
        t = threading.Thread(target=ThreadFunc(loop, (i,loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
    print('all DONE at: ', ctime())

if __name__ == '__main__':
    main()

