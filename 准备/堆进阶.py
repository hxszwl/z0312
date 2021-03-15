#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2021年3月15日 0015上午 09:39:02
# @Author:zwl(zwlhxs@163.com)
# @File:堆进阶.py
# @Software:PyCharm

# remember 记得
# ls =3
# scores  = [[None] * ls for _ in range(3)]
#
# print(scores)

from heapq import *
def  fun():
    '''

    heappush(heap,x) :将列表中元素压入堆,heap 是一个列表，x是被压入元素
    heappop(heap) ：弹出堆中最小元素
    heapify(heap) :可以让一个列表具有堆的特性，使列表本身变为堆
    heapreplace(heap,x) ：弹出最小元素，将 x压入
    nlargest(n,heap) ：返回堆中n个最大元素
    nsmallest(n,heap)
    :return:
    '''
heap = []
ls  =  [1,2,3,4,5,2,4,68,8]
for i in ls:
    heappush(heap,i)
hq = heapify(ls)
print(hq) #  None
print(ls) #  [1, 2, 2, 4, 5, 3, 4, 68, 8]
print(heap) # [1, 2, 2, 4, 5, 3, 4, 68, 8]
nl = nlargest(2,heap)
print(nl) # [68, 8]
print(heap) #  [1, 2, 2, 4, 5, 3, 4, 68, 8]
n2 = nsmallest(3,ls) #
n3 = nsmallest(13,ls)
print(n2) # [1, 2, 2]
print(n3) #  [1, 2, 2, 3, 4, 4, 5, 8, 68]

