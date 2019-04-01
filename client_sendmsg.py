#-*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source_img')
parser.add_argument('--style')
parser.add_argument('--output_dir')
opt = parser.parse_args()

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 10002))


import time

src_img = opt.source_img
style = opt.style
output_img = opt.output_dir
# flag = b'up test_img Hosoda test_output_client_2'
flag = 'up ' + src_img + ' ' + style + ' ' + output_img
# while True:
# bytes(flag, encoding = "utf8")
res = bytes(flag.encode(encoding='utf-8'))
# flag.encode('utf-8')
print(type(res))
time.sleep(0)
print('send to server with value:')
sock.send(res)
print(sock.recv(1024))
sock.close()