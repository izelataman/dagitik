

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:10:56 2015

@author: izel
"""
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
import random

mu1=random.uniform(-5,5)
print mu1
sigma1=random.uniform(0.5,1.5)
print(mu1,sigma1)
mu2=random.uniform(-5,5)
sigma2=random.uniform(0.5,1.5)
print(mu2,sigma2)

"""mu1 = 4
mu2 = -3
sigma1 = 0.95
sigma2 = 1.45"""
dizi1 = np.random.normal(mu1, sigma1, 10000)
dizi2 = np.random.normal(mu2, sigma2, 10000)

dizi2ninyuvarlanmisi = [0 for x in range(10000)]
dizi1inyuvarlanmisi  = [0 for x in range(10000)]

#print(dizi1)
"""count, bins, ignored = plt.hist(dizi1, 10, normed=True)
plt.plot(bins, 1/(sigma1 * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu1)**2 / (2 * sigma1**2) ),linewidth=2, color='r')
plt.show()

plt.hist()"""

for i in range(10000):
    dizi1inyuvarlanmisi[i]=round(dizi1[i])
    dizi2ninyuvarlanmisi[i]=round(dizi2[i])

histogramindeks = [0 for x in range(41)]
histogram2indeks = [0 for x in range(41)]


for i in range(len(dizi1inyuvarlanmisi)):
    if(dizi1inyuvarlanmisi[i]== -20):
        histogramindeks[0]= histogramindeks[0]+1
    elif(dizi1inyuvarlanmisi[i]== -19):
        histogramindeks[1]= histogramindeks[1]+1
    elif(dizi1inyuvarlanmisi[i]== -18):
        histogramindeks[2]= histogramindeks[2]+1
    elif(dizi1inyuvarlanmisi[i]== -17):
        histogramindeks[3]= histogramindeks[3]+1
    elif(dizi1inyuvarlanmisi[i]== -16):
        histogramindeks[4]= histogramindeks[4]+1
    elif(dizi1inyuvarlanmisi[i]== -15):
        histogramindeks[5]= histogramindeks[5]+1
    elif(dizi1inyuvarlanmisi[i]== -14):
        histogramindeks[6]= histogramindeks[6]+1
    elif(dizi1inyuvarlanmisi[i]== -13):
        histogramindeks[7]= histogramindeks[7]+1
    elif(dizi1inyuvarlanmisi[i]== -12):
        histogramindeks[8]= histogramindeks[8]+1
    elif(dizi1inyuvarlanmisi[i]== -11):
        histogramindeks[9]= histogramindeks[9]+1
    elif(dizi1inyuvarlanmisi[i]== -10):
        histogramindeks[10]= histogramindeks[10]+1
    elif(dizi1inyuvarlanmisi[i]== -9):
        histogramindeks[11]= histogramindeks[11]+1
    elif(dizi1inyuvarlanmisi[i]== -8):
        histogramindeks[12]= histogramindeks[12]+1
    elif(dizi1inyuvarlanmisi[i]== -7):
        histogramindeks[13]= histogramindeks[13]+1
    elif(dizi1inyuvarlanmisi[i]== -6):
        histogramindeks[14]= histogramindeks[14]+1
    elif(dizi1inyuvarlanmisi[i]== -5):
        histogramindeks[15]= histogramindeks[15]+1
    elif(dizi1inyuvarlanmisi[i]== -4):
        histogramindeks[16]= histogramindeks[16]+1
    elif(dizi1inyuvarlanmisi[i]== -3):
        histogramindeks[17]= histogramindeks[17]+1
    elif(dizi1inyuvarlanmisi[i]== -2):
        histogramindeks[18]= histogramindeks[18]+1
    elif(dizi1inyuvarlanmisi[i]== -1):
        histogramindeks[19]= histogramindeks[19]+1
    elif(dizi1inyuvarlanmisi[i]== 0):
        histogramindeks[20]= histogramindeks[20]+1
    
   
    elif(dizi1inyuvarlanmisi[i]== 20):
        histogramindeks[40]= histogramindeks[40]+1
    elif(dizi1inyuvarlanmisi[i]== 19):
        histogramindeks[39]= histogramindeks[39]+1
    elif(dizi1inyuvarlanmisi[i]== 18):
        histogramindeks[38]= histogramindeks[38]+1
    elif(dizi1inyuvarlanmisi[i]== 17):
        histogramindeks[37]= histogramindeks[37]+1
    elif(dizi1inyuvarlanmisi[i]== 16):
        histogramindeks[36]= histogramindeks[36]+1
    elif(dizi1inyuvarlanmisi[i]== 15):
        histogramindeks[35]= histogramindeks[35]+1
    elif(dizi1inyuvarlanmisi[i]== 14):
        histogramindeks[34]= histogramindeks[34]+1
    elif(dizi1inyuvarlanmisi[i]== 13):
        histogramindeks[33]= histogramindeks[33]+1
    elif(dizi1inyuvarlanmisi[i]== 12):
        histogramindeks[32]= histogramindeks[32]+1
    elif(dizi1inyuvarlanmisi[i]== 11):
        histogramindeks[31]= histogramindeks[31]+1
    elif(dizi1inyuvarlanmisi[i]== 10):
        histogramindeks[30]= histogramindeks[30]+1
    elif(dizi1inyuvarlanmisi[i]== 9):
        histogramindeks[29]= histogramindeks[29]+1
    elif(dizi1inyuvarlanmisi[i]== 8):
        histogramindeks[28]= histogramindeks[28]+1
    elif(dizi1inyuvarlanmisi[i]== 7):
        histogramindeks[27]= histogramindeks[27]+1
    elif(dizi1inyuvarlanmisi[i]== 6):
        histogramindeks[26]= histogramindeks[26]+1
    elif(dizi1inyuvarlanmisi[i]== 5):
        histogramindeks[25]= histogramindeks[25]+1
    elif(dizi1inyuvarlanmisi[i]== 4):
        histogramindeks[24]= histogramindeks[24]+1
    elif(dizi1inyuvarlanmisi[i]== 3):
        histogramindeks[23]= histogramindeks[23]+1
    elif(dizi1inyuvarlanmisi[i]== 2):
        histogramindeks[22]= histogramindeks[22]+1
    elif(dizi1inyuvarlanmisi[i]== 1):
        histogramindeks[21]= histogramindeks[21]+1

for i in range(len(histogramindeks)):
    histogramindeks[i]=histogramindeks[i]/float(10000)

print(histogramindeks)
    

for i in range(len(dizi2ninyuvarlanmisi)):
    if(dizi2ninyuvarlanmisi[i]== -20):
        histogram2indeks[0]= histogram2indeks[0]+1
    elif(dizi2ninyuvarlanmisi[i]== -19):
        histogram2indeks[1]= histogram2indeks[1]+1
    elif(dizi2ninyuvarlanmisi[i]== -18):
        histogram2indeks[2]= histogram2indeks[2]+1
    elif(dizi2ninyuvarlanmisi[i]== -17):
        histogram2indeks[3]= histogram2indeks[3]+1
    elif(dizi2ninyuvarlanmisi[i]== -16):
        histogram2indeks[4]= histogram2indeks[4]+1
    elif(dizi2ninyuvarlanmisi[i]== -15):
        histogram2indeks[5]= histogram2indeks[5]+1
    elif(dizi2ninyuvarlanmisi[i]== -14):
        histogram2indeks[6]= histogram2indeks[6]+1
    elif(dizi2ninyuvarlanmisi[i]== -13):
        histogram2indeks[7]= histogram2indeks[7]+1
    elif(dizi2ninyuvarlanmisi[i]== -12):
        histogram2indeks[8]= histogram2indeks[8]+1
    elif(dizi2ninyuvarlanmisi[i]== -11):
        histogram2indeks[9]= histogram2indeks[9]+1
    elif(dizi2ninyuvarlanmisi[i]== -10):
        histogram2indeks[10]= histogram2indeks[10]+1
    elif(dizi2ninyuvarlanmisi[i]== -9):
        histogram2indeks[11]= histogram2indeks[11]+1
    elif(dizi2ninyuvarlanmisi[i]== -8):
        histogram2indeks[12]= histogram2indeks[12]+1
    elif(dizi2ninyuvarlanmisi[i]== -7):
        histogram2indeks[13]= histogram2indeks[13]+1
    elif(dizi2ninyuvarlanmisi[i]== -6):
        histogram2indeks[14]= histogram2indeks[14]+1
    elif(dizi2ninyuvarlanmisi[i]== -5):
        histogram2indeks[15]= histogram2indeks[15]+1
    elif(dizi2ninyuvarlanmisi[i]== -4):
        histogram2indeks[16]= histogram2indeks[16]+1
    elif(dizi2ninyuvarlanmisi[i]== -3):
        histogram2indeks[17]= histogram2indeks[17]+1
    elif(dizi2ninyuvarlanmisi[i]== -2):
        histogram2indeks[18]= histogram2indeks[18]+1
    elif(dizi2ninyuvarlanmisi[i]== -1):
        histogram2indeks[19]= histogram2indeks[19]+1
    elif(dizi2ninyuvarlanmisi[i]== 0):
        histogram2indeks[20]= histogram2indeks[20]+1
    
   
    elif(dizi2ninyuvarlanmisi[i]== 20):
        histogram2indeks[40]= histogram2indeks[40]+1
    elif(dizi2ninyuvarlanmisi[i]== 19):
        histogram2indeks[39]= histogram2indeks[39]+1
    elif(dizi2ninyuvarlanmisi[i]== 18):
        histogram2indeks[38]= histogram2indeks[38]+1
    elif(dizi2ninyuvarlanmisi[i]== 17):
        histogram2indeks[37]= histogram2indeks[37]+1
    elif(dizi2ninyuvarlanmisi[i]== 16):
        histogram2indeks[36]= histogram2indeks[36]+1
    elif(dizi2ninyuvarlanmisi[i]== 15):
        histogram2indeks[35]= histogram2indeks[35]+1
    elif(dizi2ninyuvarlanmisi[i]== 14):
        histogram2indeks[34]= histogram2indeks[34]+1
    elif(dizi2ninyuvarlanmisi[i]== 13):
        histogram2indeks[33]= histogram2indeks[33]+1
    elif(dizi2ninyuvarlanmisi[i]== 12):
        histogram2indeks[32]= histogram2indeks[32]+1
    elif(dizi2ninyuvarlanmisi[i]== 11):
        histogram2indeks[31]= histogram2indeks[31]+1
    elif(dizi2ninyuvarlanmisi[i]== 10):
        histogram2indeks[30]= histogram2indeks[30]+1
    elif(dizi2ninyuvarlanmisi[i]== 9):
        histogram2indeks[29]= histogram2indeks[29]+1
    elif(dizi2ninyuvarlanmisi[i]== 8):
        histogram2indeks[28]= histogram2indeks[28]+1
    elif(dizi2ninyuvarlanmisi[i]== 7):
        histogram2indeks[27]= histogram2indeks[27]+1
    elif(dizi2ninyuvarlanmisi[i]== 6):
        histogram2indeks[26]= histogram2indeks[26]+1
    elif(dizi2ninyuvarlanmisi[i]== 5):
        histogram2indeks[25]= histogram2indeks[25]+1
    elif(dizi2ninyuvarlanmisi[i]== 4):
        histogram2indeks[24]= histogram2indeks[24]+1
    elif(dizi2ninyuvarlanmisi[i]== 3):
        histogram2indeks[23]= histogram2indeks[23]+1
    elif(dizi2ninyuvarlanmisi[i]== 2):
        histogram2indeks[22]= histogram2indeks[22]+1
    elif(dizi2ninyuvarlanmisi[i]== 1):
        histogram2indeks[21]= histogram2indeks[21]+1

for i in range(len(histogram2indeks)):
    histogram2indeks[i]=histogram2indeks[i]/float(10000)


print(histogram2indeks)

"""plt.hist(dizi1inyuvarlanmisi, bins=[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1, 0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.show()

plt.hist()"""
bins=[-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1, 0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum1 = 0

for i in range(len(histogramindeks)):
    if(histogramindeks[i] != 0):
        for j in range(len(histogram2indeks)):
            if(histogram2indeks[j] != 0):
                if(i-j<0):
                    sum1 = sum1 + histogramindeks[i] * (j-i)
                else:
                    sum1 = sum1 + histogramindeks[i] * (i-j)
        
print "Distance:" ,(sum1)

plot = plt.subplot(111)
plot.bar(bins, histogramindeks,  width=1, color = 'g') 
plot.bar(bins, histogram2indeks, width=1, color = 'r') 
plt.show()

commit changes??
