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
    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.ip = ip
        self.port = port
    def run(self):
        self.socket.connect((self.ip, self.port))

class peerServerSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        
        
    def run():
        
class peerServerRecieveMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        
        
    def run():
        
class peerClientThread (threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        
        
    def run():
    
class peerClientSendMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        
        
    def run():

class peerClientRecieveMessage(threading.Thread):
    def __init__(self, ip, port, socket, cQueue):
        
        
    def run():
        

s = socket.socket()
host = "127.0.0.1"
port = 12354
hostserver = "0.0.0.0"

serverThread = peerServerThread(host,port,s)
serverThread.start()
serverThread.join()

