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
        print "peerServer Threadi basladi"
        self.socket.connect((self.ip, self.port))
        msg = "REGME " + self.ip + ":" + str(self.port)
        self.cQueue.put(msg)
        
        clientThread = peerClientThread(host, port, s)
        clientThread.start()
        
        serverSendMessage = peerServerSendMessage(host,port,s,messageQueue1)
        serverSendMessage.start()
        
        serverReceiveMessage = peerServerReceiveMessage(host,port,s,messageQueue1)
        serverReceiveMessage.start()
        
        serverReceiveMessage.join()
        clientThread.join()
        serverSendMessage.join()
class peerServerSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, sQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.sQueue = sQueue
    def run(self):
        print "peerSErver mesaj threadi basladi"
        while True:
            if self.sQueue.qsize() > 0:
                message = self.sQueue.get()
                self.socket.send(message)
        
class peerServerReceiveMessage(threading.Thread):
    def __init__(self, ip, port, socket, sQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.sQueue = sQueue
    def parser(self,fulldata):
        if fulldata == "HELLO":
            print "HELLO"
            self.sQueue.put("SALUT P")
        if fulldata == "CLOSE":
            self.sQueue.put("BUBYE")
    def run(self):
        print "peerServer mesajalma threadi basladi"
        while True:
            fulldata = self.socket.recv(1024)
            self.parser(fulldata)
            print fulldata
        
class peerClientThread (threading.Thread):
    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket        
    def run(self):
        print "peerClient threadi basladi"
        clientReceiveMessage = peerClientReceiveMessage(host, port, s, messageQueue1)
        clientReceiveMessage.start()
        
        clientSendMessage = peerClientSendMessage(host, port, s, messageQueue1)
        clientSendMessage.start()
        
        clientReceiveMessage.join()
        clientSendMessage.join()
class peerClientSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.cQueue = cQueue
    def run(self):
        print "peerClient mesaj threadi basladi"
        while True:
            if self.cQueue.qsize() > 0:
                message = self.cQueue.get()
                self.socket.send(message)
            for index in xrange(15):
                data = raw_input("zzzz:")
                self.socket.send(data)

class peerClientReceiveMessage(threading.Thread):
    def __init__(self, ip, port, socket, sQueue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.sQueue = sQueue
    def parser(self,fulldata):
        if fulldata == "HELLO":
            print fulldata
            self.sQueue.put("SALUT P")
        if fulldata == "CLOSE":
            self.sQueue.put("BUBYE")
    def run(self):
        print "peerClient mesajalma threadi basladi"
        while True:
            fulldata = self.socket.recv(1024)
            self.parser(fulldata)
            print fulldata
        

s = socket.socket()
hostserver = "0.0.0.0"
port = 12354
host = "127.0.0.1"
messageQueue1 = Queue.Queue(10)
messageQueue2 = Queue.Queue(10)

serverThread = peerServerThread(host,port,s,messageQueue2)
serverThread.start()
serverThread.join()

