# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 16:04:30 2015

@author: Toshiba-PC
"""

import sys
import socket
import threading
import Queue
import time

class WriteThread (threading.Thread):
    def __init__(self, name, cSocket, address, threadQueue, logQueue ):
        threading.Thread.__init__(self)
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = logQueue
        self.tQueue = threadQueue
    def run(self):
        print "Starting writeThread " + self.name
        #self.lQueue.put("Starting " + self.name)
        while True:
            # burasi kuyrukta sirasi gelen mesajlari
            # gondermek icin kullanilacak
            if self.threadQueue.qsize() > 0:
                """queue_message = self.threadQueue.get()
                # gonderilen ozel mesajsa
                if queue_message[1]:
                    message_to_send = "MSG " + ...
                # genel mesajsa
                elif queue_message[1]:
                    message_to_send = "SAY " + ...
                    # hicbiri degilse sistem mesajidir
                else:
                    message_to_send = "SYS " + ..."""
    
        self.lQueue.put("Exiting " + self.name)
        
class ReadThread (threading.Thread):
    def __init__(self, name, cSocket, address, logQueue):
        threading.Thread.__init__(self)
        threadQueue = Queue.Queue()
        self.name = name
        self.cSocket = cSocket
        self.address = address
        self.lQueue = logQueue
        self.fihrist = fihrist
        self.tQueue = threadQueue
    def parser(self,data):
        data = data.strip()
        # henuz login olmadiysa
        #if not self.nickname and not data[0:3] == "USR":
        if data[0:3] == "USR":
            nickname = data[4:]
            if(self.fihrist.has_key(nickname) == False):
                # kullanici yoksa
                response = "HEL " + nickname
                self.csend(response)
                # fihristi guncelle
                self.fihrist.update({nickname:self.tQueue})
                self.lQueue.put(self.nickname + " has joined.")
                return 0
            else:
                # kullanici reddedilecek
                response = "REJ " + nickname
                self.csend(response)
                # baglantiyi kapat
                self.csoc.close()
                return 1
        elif data[0:3] == "QUI":
            response = "BYE " + self.nickname
            self.csend(response)
            # fihristten sil
            del self.fihrist[nickname]
            # log gonder
            self.lQueue.put(self.nickname + " has left.")
            # baglantiyi sil
             
        elif data[0:3] == "LSQ":
            response = "LSA "
            ...
            ...
        elif data[0:3] == "TIC":
            response = "TOC"
            self.csend(response)
            return 1
        elif data[0:3] == "SAY":
            ...
            ...
        elif data[0:3] == "MSG":
            ...
            ...
            ...
            if not to_nickname in self.fihrist.keys():
                response = "MNO"
            else:
                queue_message = (to_nickname, self.nickname, message)
                # gonderilecek threadQueueyu fihristten alip icine yaz
                self.fihrist[to_nickname].put(queue_message)
                response = "MOK"
                self.csend(response)
        else:
            # bir seye uymadiysa protokol hatasi verilecek
            response = "ERR"
            self.csend(response)
            return 0
        
    def run(self):
        print "Starting readThread " + self.name
        #self.lQueue.put("Starting " + self.name)
        while True:
            # burasi blocking bir recv halinde duracak
            # gelen protokol komutlari parserdan gecirilip
            # ilgili hareketler yapilacak
            incoming_data = clientSocket.recv(2048)
            #queue_message = parser(incoming_data)
            
            # istemciye cevap h a z r l a.
            
            # cevap veya cevaplari gondermek zere
            # threadQueue'ya yaz
            # lock mekanizmasini unutma
           
        #self.lQueue.put("Exiting " + self.name)
        print "Ending readThread " + self.name
class LoggerThread (threading.Thread):
    def __init__(self, name, logQueue, logFileName):
        threading.Thread.__init__(self)
        self.name = name
        self.lQueue = logQueue
        #self.fid = ...
    def log(self,message):
        # gelen mesaji zamanla beraber bastir
        t = time.ctime()
        self.fid.write(t)
        self.fid.flush()
    def run(self):
        self.log("Starting " + self.name)
        while True:
           
            # lQueue'da yeni mesaj varsa
            # self.log() metodunu cagir
            #to_be_logged = ...
            #self.log(to_be_logged)
        self.log("Exiting" + self.name)
        self.fid.close()
        
        
r = 0      
threadCounter = 0     
s = socket.socket()
host = "0.0.0.0"
port = 12345
s.bind((host, port))
s.listen(15)
tLock = threading.Lock()
logQueue = Queue.Queue()
fihrist = {}

while True:
    print "Waiting for connection"
    clientSocket, clientAddr = s.accept()
    print 'Got a connection from ', clientAddr
    threadQueue = Queue.Queue()
    rthread = ReadThread(threadCounter, clientSocket, clientAddr, logQueue)
    rthread.start()
    rthread.setDaemon(True)
    #rthreadQueue = Queue.Queue()
    wthread = WriteThread(threadCounter, clientSocket, clientAddr, threadQueue, logQueue)
    wthread.start()
    wthread.setDaemon(True)
    #wthreadQueue = Queue.Queue()
    threadCounter += 1
    
