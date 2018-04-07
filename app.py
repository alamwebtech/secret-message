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
    
    for file_nme in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
rename_files()