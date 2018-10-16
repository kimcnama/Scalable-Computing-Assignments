# -*- coding: utf-8 -*-
"""
@author: kiera
"""

hash_file = str(input("DES potfile loc: "))

def removeEndLn(ls = []):
    for i, x in enumerate(ls):
        if x[-1] == '\n':
            ls[i] = x[:-1]
    return ls

with open(hash_file) as f:
    pots = f.readlines()

pots = removeEndLn(pots)

updated_pots = pots
changed = 0

for i, line in enumerate(pots):
    hash_, passwd = line.split(':')
    if len(passwd) > 7:
        old_p = passwd
        passwd = passwd[:7]
        pots[i] = hash_ + ':' + passwd
        print(hash_ + " " + old_p + " -> " + passwd)
        changed += 1

target_file = str(input("Target Output File: "))

with open(target_file, 'w+') as tf:
    for line in updated_pots:
        tf.write(line + '\n')
        
tf.close()

print("\n{} lines changed\n".format(changed))
