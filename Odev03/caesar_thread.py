from random import uniform
import random

alfabe = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kaydirma = random.randint(1,26)
anahtar = [None]*26

print(kaydirma)
#print(alfabe[5])

for i in range(0,26):
    anahtar[((i + kaydirma) % 26)] = alfabe[i]
        
print(alfabe)
print(anahtar)

metin = "lorem ipsum dolor sit amet"
sifre = ""
print(alfabe.index('l'))
print(metin[0])

for i in metin:
    l = (alfabe.index(i) + kaydirma) % 26
    sifre += alfabe[l]
    
print(sifre)
