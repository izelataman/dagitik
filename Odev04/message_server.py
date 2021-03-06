# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:53:13 2015

@author: Toshiba-PC
"""


import socket
import threading
import time
import random

class myThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
        #print "Starting Thread-" + str(self.threadID)
        todo(self.clientSocket, self.clientAddr)
        #print "Ending Thread-" + str(self.threadID)
    
def todo(clientSocket,clientAddr):
    #print 'todo yu cagirdi'
    clientSocket.send("Welcome")
    tLock.acquire()
    while True:
        output = clientSocket.recv(2048)
        r = random.randint(2,120)
        print r
        if(r % 5 == 0) and output.strip() != "disconnect" :
            clientSocket.send("Su an saat: ")

        elif output.strip() == "disconnect":
            clientSocket.send("dis")
            #clientSocket.close()
            return 0
        elif output:
            print "Message received from client:"
            print output
            clientSocket.send("ok")
    tLock.release()
    time.sleep(1)

r = 0      
threadCounter = 0     
s = socket.socket()
host = "0.0.0.0"
port = 12345
s.bind((host, port))
s.listen(5)
tLock = threading.Lock()
threads = []

while True:
    print "Waiting for connection"
    clientSocket, clientAddr = s.accept()
    print 'Got a connection from ', clientAddr
    thread = myThread(threadCounter, clientSocket, clientAddr)
    thread.start()
    threads.append(thread)
    threadCounter += 1
    for t in threads: 
        t.join()
    print "Good bye \n"
