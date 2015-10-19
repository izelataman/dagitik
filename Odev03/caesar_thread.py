# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:04:06 2015

@author: Toshiba-PC
"""

l = int(input("kac karakter: "))

parca =[]
counter = 0
fo = open("C:\Users\Toshiba-PC\Desktop\Dagitik\metin.txt","r")
text = fo.read(l)
while text != "":
    parca.append(text)
    counter += l
    fo.seek(counter)
    text = fo.read(l)
    
print(parca)
fo.close()


fh = open("C:\Users\Toshiba-PC\Desktop\Dagitik\sifre.txt","w")
for i in range(len(parca)):
    fh.write(parca[i])
fh.close()


alfabe = list("abcdefghijklmnopqrstuvwxyz")
#s = random.randint(1,25)
s = 7
#print(s)

anahtar = [None]*26

for i in range(0,26):
    anahtar[(i + s) % 26] = alfabe[i]

anahtar = [element.upper() for element in anahtar]
#print(anahtar)
fm = open("C:\Users\Toshiba-PC\Desktop\Dagitik\sifre.txt","r")
sifrelenecekmetin = fm.read()
fm.close()

print(sifrelenecekmetin)
#metin = "lorem ipsum.Dolor!- sit amet"
sifre = ""
lower = sifrelenecekmetin.lower()
for i in range(0,len(lower)):
    if(any(map(lambda each: each in alfabe, lower[i]))):
        sifre += anahtar[(alfabe.index(str(lower[i])))]
    else:
        sifre += lower[i]

fk =  open("C:\Users\Toshiba-PC\Desktop\Dagitik\sifre.txt","w")
fk.write(sifre)
fk.close()
