# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:26:31 2018

@author: kiera
"""

import sys

file = "C:\\Users\\kiera\\Downloads\\ultimate.txt"

i = 0

with open(file) as f:
    passwrds = []
    try
    for line in f:
        i +=1
        print(line)
        passwrds.append(line)
        
    except Exception:
        sys.exc_clear()
"""
maxlen = int(input("max password length: "))
   
new_file = str(curr_dir + '\\' + input("Enter new file name: "))

with open(new_file, 'w+') as out:
    for i in range(len(passwrds)):
        if int(len(passwrds[i])) <= maxlen:
            out.write(str(passwrds[i]))
        
out.close()

"""