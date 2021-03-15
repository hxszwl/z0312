#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2021年3月1日 0001上午 10:24:15
# @Author:zwl(zwlhxs@163.com)
# @File:客户端.py
# @Software:PyCharm

import socket

'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in ['a', 'b', 'c']:
    # 发送数据:
    data =data.encode()
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024))

s.close()