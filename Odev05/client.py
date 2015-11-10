# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:50:13 2015

@author: Toshiba-PC
"""


#!/usr/bin/env python
import socket
import threading
import sys
import time
import Queue

class ReadThread (threading.Thread):
    def __init__(self, name, csoc, threadQueue, app):
        threading.Thread.__init__(self)
        self.name = name
        self.csoc = csoc
        self.nickname = ""
        self.threadQueue = threadQueue
        self.app = app
    def incoming_parser(self, data):
        ...
        ...
        ...
        ...
    def run(self):
        while True:
            data = self.csoc.recv(1024)
            ...
            ...
            ...

class WriteThread (threading.Thread):
    def __init__(self, name, csoc, threadQueue):
        threading.Thread.__init__(self)
        self.name = name
        self.csoc = csoc
        self.threadQueue = threadQueue
    def run(self):
        ...
        ...
        ...
        if self.threadQueue.qsize() > 0:
            queue_message = self.threadQueue.get()
            ...
            ...
            ...
            try:
                self.csoc.send(queue_message)
            except socket.error:
                self.csoc.close()
                break

"""class writeThread (threading.Thread):
    def __init__(self, threadID, clientSocket, clientAddr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.clientSocket = clientSocket
        self.clientAddr = clientAddr
    def run(self):
         #print "Starting writeThread " + self.name
         tLock.acquire()
         while True:
            for index in xrange(15):
                data = raw_input("zzzz:")
                s.send(data)
                msg = s.recv(2048)
                if msg == "dis":
                    print "Disconnecting"
                    s.close()
                    sys.exit("Received disconnect message.  Shutting down.")
                elif msg == "Su an saat: ":
                    print "Su an saat: " + time.strftime("%H:%M:%S")
                elif msg == "ok":
                    print "PEKI" + "    <" + str(host) + ">"
               
         #print "Exiting writeThread " + self.name 
         tLock.release()
         time.sleep(1)"""
         
s = socket.socket()
host = ...
port = ...
s.connect((host,port))
sendQueue = ...
app = ClientDialog(sendQueue)
# start threads
rt = ReadThread("ReadThread", s, sendQueue, app)
rt.start()

wt = WriteThread("WriteThread", s, sendQueue)
wt.start()

rt.join()
wt.join()
s.close()

