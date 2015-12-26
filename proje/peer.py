# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:35:37 2015

@author: Toshiba-PC
"""
import Queue
import time
import socket
import sys
import threading

class peerServerThread (threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        threading.Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
        self.cQueue = cQueue
    def run(self):
        self.socket.connect((self.ip, self.port))
        msg = "REGME " + self.ip + ":" + str(self.port)
        self.cQueue.put(msg)
        clientThread = peerClientThread(host, port, s)
        clientThread.start()
        clientThread.join()
        
        serverSendMessage = peerServerSendMessage()

class peerServerSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, sQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.sQueue = sQueue
    def run(self):
        while True:
            if self.sQueue.qsize() > 0:
                message = self.sQueue.get()
                self.socket.send(message)
        
class peerServerRecieveMessage(threading.Thread):
    def __init__(self, ip, port, socket, sQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.sQueue = sQueue
    def parser(self,fulldata):
        if fulldata == "HELLO":
            self.sQueue.put("SALUT P")
        if fulldata == "CLOSE":
            self.sQueue.put("BUBYE")
    def run(self):
        while True:
            fulldata = self.cSocket.recv(1024)
            print fulldata
        
class peerClientThread (threading.Thread):
    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket        
    def run(self):
        clientSendMessage = peerClientSendMessage(host, port, s, messageQueue1)
        clientSendMessage.start()
        clientSendMessage.join()
        
        clientReceiveMessage = peerClientReceiveMessage(host, port, s)
        clientReceiveMessage.start()
        clientReceiveMessage.join()
    
class peerClientSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.cQueue = cQueue
    def run(self):
        while True:
            if self.cQueue.qsize() > 0:
                message = self.cQueue.get()
                self.socket.send(message)
            for index in xrange(15):
                data = raw_input("zzzz:")
                self.socket.send(data)

class peerClientReceiveMessage(threading.Thread):
    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket       
    def run(self):
        while True:
            fulldata = self.cSocket.recv(1024)
            self.clientParser(fulldata)
        

s = socket.socket()
host = "127.0.0.1"
port = 12354
hostserver = "0.0.0.0"
messageQueue1 = Queue.Queue(10)
messageQueue2 = Queue.Queue(10)

serverThread = peerServerThread(host,port,s,messageQueue2)
serverThread.start()
serverThread.join()

