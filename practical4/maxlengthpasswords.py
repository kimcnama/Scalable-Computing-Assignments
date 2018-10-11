# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:26:31 2018

@author: kiera
"""

import os

curr_dir = os.getcwd()

file = str(curr_dir + '\\' + input("Enter file name: "))

with open(file) as f:
    passwrds = f.readlines()
 
maxlen = int(input("max password length: "))
   
new_file = str(curr_dir + '\\' + input("Enter new file name: "))

with open(new_file, 'w+') as out:
    for i in range(len(passwrds)):
        if int(len(passwrds[i])) <= maxlen:
            out.write(str(passwrds[i]))
        
out.close()

