# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:50:43 2018

@author: kieran
"""

import os

def removeEndLn(ls = []):
    for i, x in enumerate(ls):
        if x[-1] == '\n':
            ls[i] = x[:-1]
    return ls

files = os.listdir()
curr_dir = os.getcwd()
toCrack = []
otherHashes = []

for f in files:
    if f != 'hash_comparator.py':
        if f[f.find('.'):] == '.hashes':
            with open(curr_dir + '\\' + f, "r") as r1:
                toCrack.append(r1.readlines())
        else:
            with open(curr_dir + '\\' + f, "r") as r2:
                otherHashes.append(r2.readlines())

to_crack = []
other_hashes = []
for i in range(len(toCrack)):
    for h in toCrack[i]:
        to_crack.append(h)
        
for i in range(len(otherHashes)):
    for h in otherHashes[i]:
        other_hashes.append(h)

other_hashes = removeEndLn(other_hashes)
to_crack = removeEndLn(to_crack)

cracked = {}

for i in other_hashes:
    i = i.replace(' ', ':')
    ind = i.find(':')
    cracked[i[:ind]] = i[ind+1:]

matches = 0

for i in to_crack:
    if i in cracked.keys():
        print(cracked[i])
        matches += 1

print(matches)


