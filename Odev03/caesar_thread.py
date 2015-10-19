# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import uniform
import random

alfabe = list("abcdefghijklmnopqrstuvwxyz")
#s = random.randint(1,25)
s = 7
#print(s)

anahtar = [None]*26

for i in range(0,26):
    anahtar[(i + s) % 26] = alfabe[i]

anahtar = [element.upper() for element in anahtar]
print(anahtar)

metin = "lorem ipsum dolor sit amet"
sifre = ""

for i in range(0,26):
    if(any(map(lambda each: each in alfabe, metin[i]))):
        sifre += anahtar[(alfabe.index(str(metin[i])))]
    else:
        sifre += " "
print(sifre)
        
    
#print(alfabe.index(str(metin[6])))
    
