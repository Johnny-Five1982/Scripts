#!/usr/bin/env python
import socket, sys
try:
    with open(sys.argv[1], "r") as ins: # "resolve.txt"
        for line in ins:
            print ("Address: " + line.strip() + " Resolved: " + socket.gethostbyname(line.strip()) )
except socket.error:
    pass
