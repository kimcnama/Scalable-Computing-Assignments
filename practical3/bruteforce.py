# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:26:18 2018

@author: kiera
"""

length = int(input("Input number of characters: "))

upper, lower = 52, 26

if input("Include capitals? (y/n): ") == 'y':
    caps = True
    char_dom, iterations = upper, upper
else:
    caps = False
    char_dom, iterations = lower, lower

test = ''

for i in range(0, length):
    test += 'a'
    if caps == True:
        iterations *= upper
    else:
        iterations *= lower
        
index = 0

for i in range(1, iterations + 1):
    print(test)
    """
    do hash
    """
    
    test[0] = chr(ord(test[0] + 1))
    if test[0] == '{':
        ind = 1
        while(test[ind] == 'z'):
            test[ind] = 'a'
    
    
        
        while(pivot < length):
            test[pivot] = 'a'
            
        
        
        
    if iterations % 26:
        index = length - 1
        while(test[index] == 'z'):
            reset = True
            test[index] = 'a' 
            index -= 1
        if reset == True:
            test[index] = chr(ord(test[index] + 1))
    
    
    
    
    
    
    
    
    
    
    
        
    