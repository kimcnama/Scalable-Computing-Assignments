# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:19:12 2018

@author: kiera
"""
import os

curr_dir = os.getcwd()

hash_file = 'C:\\git\\Scalable-Computing-Assignments\\practical4\\SHA512.hashes'
pot_file = 'C:\\git\\Scalable-Computing-Assignments\\practical4\\submission6.broken'

def removeEndLn(ls = []):
    for i, x in enumerate(ls):
        if x[-1] == '\n':
            ls[i] = x[:-1]
    return ls

with open(hash_file) as f1:
    hashes = f1.readlines()
    
with open(pot_file) as f2:
    pots = f2.readlines()

hashes = removeEndLn(hashes)
pots = removeEndLn(pots)

pots = [x[:x.find(':')] for x in pots]

yet_to_crk = str(curr_dir + '\\' + input("Enter new file name: "))

matches = 0
left = 0

with open(yet_to_crk, 'w+') as ytc:
    for h in hashes:
        if h not in pots:
            ytc.write(str(h) + '\n')
            left += 1
        else:
            matches += 1
        
ytc.close()

print("\nYou have {} cracked\n".format(matches))
print("There are {} left".format(left))
