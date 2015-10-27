# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:20:18 2015

@author: Toshiba-PC
"""

#!/usr/bin/env python
import socket
s = socket.socket()
host = "127.0.0.1"
port = 12345
s.connect((host, port))
print s.recv(1024)
