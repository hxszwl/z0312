#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2021年3月12日 0012下午 03:49:39
# @Author:zwl(zwlhxs@163.com)
# @File:python的进阶学习.py
# @Software:PyCharm

def selelct_sort(item,comp = lambda x,y : x > y):
    '''
    选择排序
    :param item:
    :param comp:
    :return:
    '''

# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# def get(k):
#     print(k,'k')
#     return salaries[k]
# print(max(salaries,key=get)) #'alex'
# print(max(salaries,key=lambda x:salaries[x]))

d = {'d1':2, 'd2':4, 'd4':1,'d3':3,}
res = sorted(d.items(),key=lambda d:d[1])
print(res)