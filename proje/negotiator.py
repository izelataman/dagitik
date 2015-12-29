# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:23:33 2015

@author: Toshiba-PC
"""
import Queue
import time
import socket
import sys
import threading

class negotiatorServerThread (threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        threading.Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
        self.cQueue = cQueue
    def run(self):
        print "hello server thread basladi"
        self.socket.bind((self.ip, self.port))
        self.socket.listen(5)
        print "Waiting for connection"
        while True:
            clientSocket, clientAddr = self.socket.accept()
            print 'Got a connection from ', clientAddr
            connQueue.put(clientSocket)
            connQueue.put(clientAddr)
            
            clientThread = negotiatorClientThread(host, port, s, clientSocket, clientAddr, CONNECT_POINT_LIST, messageQueue2)
            clientThread.start()           
            #self.cQueue.put("HELLO")
            serverSendMessage = negotiatorServerSendMessage(clientSocket, clientAddr, CONNECT_POINT_LIST, messageQueue1)
            serverSendMessage.start()

            serverRecieveMessage = negotiatorServerRecieveMessage(clientSocket, clientAddr, CONNECT_POINT_LIST, messageQueue2, messageQueue1)
            serverRecieveMessage.start()
            
            #serverRecieveMessage.join()
            #serverSendMessage.join()
            #clientThread.join()
class negotiatorServerSendMessage(threading.Thread):
    #answer: REGWA to peer client 
    def __init__(self, cSocket, cAddr, CPlist,sQueue): 
        threading.Thread.__init__(self)
        self.cSocket = cSocket
        self.cAddr = cAddr
        self.CPlist = CPlist
        self.sQueue = sQueue
    def run(self):
        print "negoServer mesaj threadi basladi"
        while True:
            if self.sQueue.qsize() > 0:
                message = self.sQueue.get()
                self.cSocket.send(message)
        
    
class negotiatorServerRecieveMessage(threading.Thread):
        #REGME
        #GETNL
    def __init__(self, cSocket, cAddr, CPlist, cQueue, sQueue):
        threading.Thread.__init__(self)
        self.cSocket = cSocket
        self.cAddr = cAddr
        self.CPlist = CPlist
        self.cQueue = cQueue
        self.sQueue = sQueue
    def serverParser(self,fulldata):
        data = fulldata.split(" ")
        if data[0] == "REGME":
            self.sQueue.put("REGWA \n")
            self.cQueue.put("HELLO")          
            dataAddr = data[1].split(":")
            #Nself.CPlist[dataAddr[0], dataAddr[1]] = ("?","W")
        elif data[0] == "GETNL":
            self.sQueue.put("NLIST BEGIN:")
            s = []
            m = []
            mssg = ""
            for i in range(len(CONNECT_POINT_LIST)):
                s = CONNECT_POINT_LIST.keys()[i]
                m = CONNECT_POINT_LIST.values()[i]
                mssg = str(s) + ":" + str(m)
                self.sQueue.put(mssg)
                #print mssg
            self.sQueue.put("NLIST END:")
        else:
            print "elelel"
            #self.sQueue.put("hadi bakalim")
    def run(self):
        print "negoServer mesajalma threadi basladi"
        while True:
            fulldata = self.cSocket.recv(1024)
            self.serverParser(fulldata)

class negotiatorClientThread (threading.Thread):
    def __init__(self, ip, port, socket, cSocket, cAddr, CPlist, cQueue ):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.cSocket = cSocket
        self.cAddr = cAddr
        self.CPlist = CPlist
        self.cQueue = cQueue
    def run(self):
        print "hello ben istemci"
        clientSocket = connQueue.get()
        clientAddr = connQueue.get()
        #print "NegoClient Receive in dinledigi ve mesaj yoolladigiport:"
        #print clientSocket
        #print clientAddr
        clientReceiveMessage = negotiatorClientRecieveMessage(clientSocket, clientAddr, CONNECT_POINT_LIST)
        clientReceiveMessage.start()
        
        clientSendMessage = negotiatorClientSendMessage(host, port, s, clientSocket, clientAddr, CONNECT_POINT_LIST, messageQueue2)
        clientSendMessage.start()
        
        clientSendMessage.join()
        clientReceiveMessage.join()
        
class negotiatorClientSendMessage(threading.Thread):
    def __init__(self,ip, port, socket, cSocket, cAddr, CPlist,cQueue):
        # HELLO
        # CLOSE
        # REGWA
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.cSocket = cSocket
        self.cAddr = cAddr
        self.CPlist = CPlist  
        self.cQueue = cQueue
    def run(self):
        print "negoClient mesaj threadi basladi"
        while True:
            if self.cQueue.qsize() > 0:
                message = self.cQueue.get()
                self.cSocket.send(message)
class negotiatorClientRecieveMessage(threading.Thread):
    #SALUT
    #BUBYE
    def __init__(self, cSocket, cAddr, CPlist):
        threading.Thread.__init__(self)
        self.cSocket = cSocket
        self.cAddr = cAddr
        self.CPlist = CPlist
    def clientParser(self,fulldata):
        print fulldata
        data = fulldata.split(" ")
        if(data[0]=="SALUT"):
            if (data[1]=="P"):
                self.CPlist[self.cAddr] = ("P", "S")
            if (data[1]=="N"):
                self.CPlist[self.cAddr] = ("N", "S")
        elif(data[0] == "BUBYE"):
            self.cSocket.close()
            sys.exit("Received disconnect message.  Shutting down.")
        else:
            print "ellele"
        print "conn.point list ::::\n" 
        print CONNECT_POINT_LIST
        
    def run(self):
        print "negoClient mesajalma threadi basladi"
        while True:
            fulldata = self.cSocket.recv(1024)
            self.clientParser(fulldata)
            
CONNECT_POINT_LIST = {}
messageQueue1 = Queue.Queue(10)
messageQueue2 = Queue.Queue(10)
connQueue = Queue.Queue(10)
s = socket.socket()
host = "127.0.0.1"
port = 12354
while True:
    serverThread = negotiatorServerThread(host, port, s, messageQueue2)
    serverThread.start()
    serverThread.join()
    
   
    
