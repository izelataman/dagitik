# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:15:39 2015

@author: Toshiba-PC
"""

from random import uniform
import random

import threading 
import Queue
import time

s = int(input("sifreleme icin kac tane kaydiralim: "))
n = int(input("thread sayisi: "))
l = int(input("kac karakter: "))

alfabe = list("abcdefghijklmnopqrstuvwxyz")
anahtar = [None]*26
for i in range(0,26):
    anahtar[(i + s) % 26] = alfabe[i]
anahtar = [element.upper() for element in anahtar]
print alfabe
print(anahtar)
print "\n"
  
  
exitFlag = 0
counter = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
         threading.Thread.__init__(self)
         self.threadID = threadID
         self.name = name
         self.q = q
    def run(self):
         print "Starting " + self.name
         process_data(self.name, self.q)
         print "Exiting " + self.name 

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            sifre = ""
            for i in range(0,len(data)):
                if(any(map(lambda each: each in alfabe, data[i]))):
                    sifre += anahtar[(alfabe.index(str(data[i])))]
                else:
                    sifre += data[i]
                    
            fk =  open("C:\Users\Toshiba-PC\Desktop\Dagitik\crypted_"+str(s)+"_"+str(n)+"_"+str(l)+".txt","a+")
            fk.write(sifre)
            fk.close()
                
            queueLock.release()
            #print "%s processing %s \n" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1) 

parca =[]
counter = 0
fo = open("C:\Users\Toshiba-PC\Desktop\Dagitik\metin.txt","r")
text = fo.read(l)
while text != "":
   text = text.lower()
   parca.append(text)
   counter += l
   fo.seek(counter)
   text = fo.read(l)
fo.close()
    
print parca

#nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(len(parca))
threads = []
threadID = 1

# Create new threads
for i in range(1,n+1):
    thread = myThread(threadID, "thread"+str(i)+"\n", workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

    
    
# Fill the queue
queueLock.acquire()
for word in parca:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1  

# Wait for all threads to complete
for t in threads: 
    t.join()
print "Exiting Main Thread \n"









