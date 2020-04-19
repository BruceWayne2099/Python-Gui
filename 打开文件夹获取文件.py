#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#作者：ChrisChan
#用途：
import tkinter as tk
from tkinter import filedialog
import zipfile

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)
