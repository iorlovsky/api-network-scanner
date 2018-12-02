#!/usr/bin/python3.6

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
res = s.recvfrom(65565)

print(res)