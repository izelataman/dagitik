
#!/usr/bin/env python
import socket
import threading
import random
import sys
import time

class readThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
         print "Starting readThread " + str(self.threadID)
         tLock.acquire()
         print s.recv(1024)
         tLock.release()         
         print "Exiting readThread" + str(self.threadID) 


class writeThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
         print "Starting writeThread " + self.name
         
         while True:
            for index in xrange(15):
                data = raw_input("zzzz:")
                tLock.acquire()
                s.send(data)
                if(data == "disconnect"):
                    print "Disconnecting"
                    s.close()
                print s.recv(2048)+ "   <" + str(host) + ">",
                tLock.release()
         print "Exiting writeThread " + self.name 
         
         time.sleep(1)
         
tLock = threading.Lock()
rThreadCounter = 0
wThreadCounter = 0
rthreads = []
wthreads = []
s = socket.socket()
host = "127.0.0.1"
hostserver = "0.0.0.0"
port = 12345
s.connect((host, port))

while True:
        
    rThread = readThread(rThreadCounter, s, host)
    rThread.start()
    rThreadCounter += 1
    rthreads.append(rThread)

    
    wThread = writeThread(wThreadCounter, s, host)
    wThread.start()
    wThreadCounter += 1
    wthreads.append(wThread)
    
    for t in rthreads: 
        t.join()
    for t in wthreads: 
        t.join()
    
