#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2020年12月17日 0017下午 03:04:18
# @Author:zwl(zwlhxs@163.com)
# @File:多线程版本.py
# @Software:PyCharm

import datetime
import crcmod
from binascii import unhexlify
import modbus_tk
import time
import socket
import serial
from modbus_tk import modbus_rtu
from modbus_tk import defines as cst
import logging
import queue
import threading


class Connect_modbus():
    def __init__(self, list_id,port):
        self.port = (port if port else 'com2')
        self.flags = 0
        self.my_serial_flag= [100 if i == 0 else 0 for i in range(len(list_id)+1)]
        self.my_serial = None
        self.my_serial = (self.my_serial if self.my_serial else self.my_func_serial())

    def get_datas(self, slave_id, start_addr, date_len):
        try:
            holding_date = self.master.execute(slave_id, cst.READ_HOLDING_REGISTERS, start_addr, date_len)
            holding_data125 = list()
            for i in range(len(holding_date)):
                holding_data125.append('%04x' % (holding_date)[i])  # append()在Tmp1列表末尾添加新的对象
            all_holding_data = '0103' + '%02x' % (date_len * 2) + ''.join(holding_data125)
            print('为线程显示', all_holding_data)
            self.my_serial_flag[slave_id] = 0
            return str(all_holding_data)
        except Exception as e:
            print('单个子站引发','***',slave_id)

            if self.my_serial_flag[slave_id] >= 10:
                print(111)
                pass
            else:
                print(222)
                self.my_serial_flag[slave_id] += 1
                print(221)
            if all(v > 0 for v in self.my_serial_flag):
                self.flags = 1
            if self.flags:  # 如果flags被标记为1才去重新获取连接
                self.reload_serial(slave_id)
                self.flags = 0
            print(e, '后序做日志')
            return None

    def my_func_serial(self):
        while 1:
            try:
                self.my_serial = serial.Serial(port=self.port,
                                               baudrate='38400',
                                               bytesize=8,
                                               parity='N',
                                               stopbits=1,
                                               xonxoff=0)
                self.master = modbus_rtu.RtuMaster(self.my_serial)
                self.master.set_timeout(1)
                return self.my_serial
            except Exception as e:

                print(e, '第一次端口不能成功建立', self.my_serial_flag)
                time.sleep(2)
                if self.my_serial:
                    self.my_serial.close()

    def reload_serial(self, slave_id):
        '''
        重置端口
        :param slave_id:
        :return:
        '''

        while 1:

            try:
                time.sleep(1)

                if all(v > 0 for v in self.my_serial_flag):  # 判断全部标记大于0
                    self.my_serial = serial.Serial(port=self.port,
                                                   baudrate='38400',
                                                   bytesize=8,
                                                   parity='N',
                                                   stopbits=1,
                                                   xonxoff=0)
                    self.my_serial_flag[slave_id] = 1
                    self.master = modbus_rtu.RtuMaster(self.my_serial)
                    self.master.set_timeout(1)
                    ############# 成功一次，要重置flags
                    return self.my_serial
                else:
                    pass
            except Exception as e:
                print(e, '引发整个端口重置', self.my_serial_flag)
                self.my_serial_flag[slave_id] += 1
                time.sleep(2)
                if self.my_serial:
                    self.my_serial.close()