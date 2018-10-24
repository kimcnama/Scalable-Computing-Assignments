# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:52:40 2018

@author: kiera
"""

import argon2 as a2
from pwgen import pwgen
import pandas as pd
import os 
import numpy as np

hashf = "C:\\git\\Scalable-Computing-Assignments\\practical4\\Arg2i.hashes"

with open(hashf, "r") as hf:
    hashes = hf.readlines()

max_passwrd_len = 6
            
passwords = []

print("Creating Dictionary")
for i in range(max_passwrd_len):
    passwords.append(pd.unique(pwgen(i+1, 10000, no_numerals=True, no_capitalize=True)))
print("Dictionary Created")

for i, h in enumerate(hashes):
    if h[-1] == '\n':
        hashes[i] = h[:-1]

potfile = os.getcwd() + "\\" + input("Potfile name: ")

ph = a2.PasswordHasher()

total = 0
for i in range(max_passwrd_len):
    total += len(passwords[i])

iteration = 0
progress = np.arange(1, total, int(total/100))

print("To interrupt, hit Ctrl-C")
with open(potfile, "w+") as pot:
    for i in range(max_passwrd_len):
        for pswrd in passwords[i]:
            iteration += 1
            if iteration in progress:
                percentage = int(iteration * 100.00 / total)
                print("{0} / {1} ....... {2} %\n".format(iteration, total, percentage))
            hsh = ph.hash(pswrd)
            
            if hsh in hashes:
                print(hsh + ':' + pswrd + '\n')
                pot.write(hsh + ':' + pswrd + '\n')
                

pot.close()






