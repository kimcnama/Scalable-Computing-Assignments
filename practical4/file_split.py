# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:24:40 2018

@author: kieran
"""

hash_types = {'':'DES.hashes' 
              ,'$1$':'MD5.hashes' 
              ,'$5$':'SHA256.hashes' 
              ,'$6$':'SHA512.hashes' 
              ,'$argon2i$':'Arg2i.hashes' 
              ,'$pbkdf2-sha256$':'PBKDF2_SHA256.hashes' 
              }

def detHash(h):
    h = str(h)
    
    if h[0] != '$':
        return ''
    
    i = 1
    while i < len(h) and i < 16:
        if h[i] == '$':
            return h[:i+1]
        i += 1
        
    return ''

values = list(hash_types.values())

with open('C:\\git\\Scalable-Computing-Assignments\\practical4\kimcnama.hashes') as ff:
    hashes = ff.readlines()

hashes_split = 0

files = []

for i in values:
    files.append(open(i, "w+"))

for h in range(len(hashes)):
    
    for i in range(len(hash_types)):
        if hash_types[detHash(hashes[h])] == files[i].name:
            
            files[i].write(hashes[h])
            hashes_split += 1
            
for i in range(len(files)):
    files[i].close()
    
print("Hashes Split: {0} of {1}".format(hashes_split, len(hashes)))
    


