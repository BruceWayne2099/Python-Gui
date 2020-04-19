#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#作者：ChrisChan
#用途：
from tkinter import *

'''
Scale组件设置一个指定范围
只需要指定它的from和to两个选项即可，但由于from本身是python关键字
所以为了区分需要在后边紧跟一个下划线：from_
'''
root = Tk()
s1 = Scale(root, from_=0, to=42)  # Scale组件
s1.pack()
s2 = Scale(root, from_=0, to=2000, orient=HORIZONTAL)  # orient=HORIZONTAL设置水平方向显示
s2.pack()


def show():
    print('水平位置读数:', s1.get(), '\n''垂直位置读数:', s2.get())


Button(root, text='获取位置', command=show).pack()

mainloop()