# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:15:39 2015

@author: Toshiba-PC
"""
#!/usr/bin/env python
from multiprocessing import Lock, Process, Queue, current_process

n = int(input("thread sayisi: "))
l = int(input("kac karakter: "))
s = int(input("sifreleme icin kac tane kaydiralim: "))
alfabe = list("abcdefghijklmnopqrstuvwxyz")
anahtar = [None]*26
for i in range(0,26):
    anahtar[(i + s) % 26] = alfabe[i]
anahtar = [element.upper() for element in anahtar]
print alfabe
print(anahtar)
print "\n"
lo = Lock()

def worker(work_queue, done_queue): 
    print("hello workerkilitlemedim")
    lo.acquire()
    print("hello worker")
    try: 
        print("workerdayiz")
        for data in iter(work_queue.get, 'STOP'): 
            sifre = ""
            for i in range(0,len(data)):
                if(any(map(lambda each: each in alfabe, data[i]))):
                    sifre += anahtar[(alfabe.index(str(data[i])))]
                else:
                    sifre += data[i]
                    
            fk =  open("C:\Users\Toshiba-PC\Desktop\Dagitik\sifre.txt","a")
            fk.write(sifre)
            fk.close()
            done_queue.put("%s - %s got %s." % (current_process().name, data)) 
    except Exception, e: 
        done_queue.put("%s failed on %s with: %s" % (current_process().name, data)) 
        print("ERROR!!")

    lo.release()    
    return True
    
"""  
def print_site_s5
tatus(url): 
    http = httplib2.Http(timeout=10) 
    headers, content = http.request(url) 
    return headers.get('status', 'no response')"""
    
def main(): 
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
        
    #print parca

    work_queue = Queue()
    done_queue = Queue()
    processes = []
    
    for data in parca: 
        work_queue.put(data)
        
    for w in xrange(n): 
        p = Process(target=worker, args=(work_queue, done_queue)) 
        p.start() 
        processes.append(p) 
        work_queue.put('STOP')
    print processes
    
    for p in processes: 
        p.join()
    done_queue.put('STOP')
    for status in iter(done_queue.get, 'STOP'): 
        print status
if __name__ == '__main__': main()
