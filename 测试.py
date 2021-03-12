#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2020年12月16日 0016下午 05:13:28
# @Author:zwl(zwlhxs@163.com)
# @File:测试.py
# @Software:PyCharm

x = {k :0 for k in range(1,3)}
x[1] =2
# for i in x:
#     if x[i] == 0:
#         print(1)
#     else:
#         print(2)
# x1 = all(v > 0 for v in x.values())
# print(x1)
# print(x)
# 列表生成式中 if在前面
# y = [0 if x %2 ==0 else x for x in range(10)]
# print(y)
# y1 = [x for x in range(10) if x %2 ==0]
# print(y1)

list_id = ['6101','6102','6103']
a1 = [100 if i == 0 else 0 for i in range(len(list_id)+1)]
# a1[1] += 1
# a1[3] += 1
# a1[2] += 1
# x1 = all(v > 0 for v in a1 if v != a1[0])
# print(x1)
# a1[1] += 1
# print(a1)
a1[1] +=1
a1[1] +=1
a1[1] +=1
print(a1)
# dd = all(v > 0 for v in a1)
# print(dd)