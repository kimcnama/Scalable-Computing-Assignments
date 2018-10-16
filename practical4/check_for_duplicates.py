# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:36:41 2018

@author: kiera
"""

def removeEndLn(ls = []):
    for i, x in enumerate(ls):
        if x[-1] == '\n':
            ls[i] = x[:-1]
    return ls

file = "C:\\Users\\kiera\\Documents\\MAI\\Scalable Computing\\Assignments\\practical4\\submission2.broken"

with open(file) as f:
    lines = f.readlines()

lines = removeEndLn(lines)
addressed = []
dups = 0

for i, l in enumerate(lines):
    search_arr = lines[:i] + lines[(i+1):]
    if l in search_arr and l not in addressed:
        print(l)
        addressed.append(l)
        dups += 1

print("\n{} duplicates\n".format(dups))

removals = 0

for dup in addressed:
    lines.remove(dup)
    removals += 1
    
target_f = "C:\\Users\\kiera\\Documents\\MAI\\Scalable Computing\\Assignments\\practical4\\submission3.broken"
    
with open(target_f, 'w+') as tf:
    for l in lines:
        tf.write(l + '\n')
        
tf.close()
print("Removals: {}".format(removals))

