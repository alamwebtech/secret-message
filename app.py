# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 13:43:37 2018

@author: ferar
"""

import os
def rename_files():
    file_list = os.listdir(r"C:\Users\ferar\Desktop\PROJECTS\msg\prank")
    print(file_list)
    os.chdir(r"C:\Users\ferar\Desktop\PROJECTS\msg\prank")
    saved_path= os.getcwd()
    #print("Current Path" + saved_path)
    for file_name in file_list:
        trans = str.maketrans("","0123456789")
        os.rename(file_name, file_name.translate(trans))
    os.chdir(saved_path)
rename_files()