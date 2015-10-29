# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:20:18 2015

@author: Toshiba-PC
"""
"""
#!/usr/bin/env python
import socket
s = socket.socket()
host = "127.0.0.1"
port = 12345
s.connect((host, port))
print s.recv(1024)
"""

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
         while True:
            for index in xrange(15):
                data = raw_input("zzzz:")
                s.send(data)
                wThread = writeThread(threadCounter, s, host)
                mssg = wThread.start()
                print mssg
                if mssg != "None":
                    print "Disconnecting"
                    s.close()
                    sys.exit("Received disconnect message.  Shutting down.")
                elif mssg:
                    print "PEKI" + "    <" + str(host) + ">"
               
         print "Exiting writeThread " + self.name 
         wThread.join()
         tLock.release()         
         print "Exiting readThread" + str(self.threadID) 
         time.sleep(1)

class writeThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
         print "Starting writeThread " + self.name
         #tLock.acquire()
         msg = s.recv(2048)
         return msg
         #tLock.release()
         
tLock = threading.Lock()
threadCounter = 0
s = socket.socket()
host = "127.0.0.1"
hostserver = "0.0.0.0"
port = 12345
s.connect((host, port))


rThread = readThread(threadCounter, s, host)
rThread.start()
rThread.join()
