# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:15:27 2018

@author: kiera
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:19:12 2018

@author: kiera
"""

hash_file = ''
pot_file = ''

with open(hash_file) as f1:
    pot1 = f1.readlines()
    
with open(pot_file) as f2:
    pot2 = f2.readlines()        

unique = 0

out_file = ''

with open(out_file, 'w+') as of:
    for h1 in pot1:
        if h1 in pot2:
            pot2 = pot2.remove(h1)
            of.write(h1)
            unique += 1
    for h2 in pot2:
        of.write(h2)
        unique += 1
        
of.close()

print("\nUnique number cracked: {} \n".format(unique))
