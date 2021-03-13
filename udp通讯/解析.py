#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2021年3月1日 0001上午 10:37:26
# @Author:zwl(zwlhxs@163.com)
# @File:解析.py
# @Software:PyCharm
# a = b'\xe5\xa4\xa7\xe5\xae\xb6'
# print(type(a))
# print(a.decode('utf-8'))

# def is_symmetrical(str):
#
#     length = int(len(str))
#
#     for index in range(length // 2):
#         if str[index] == str[length - index - 1]:
#             pass
#
#         else:
#
#             return False
#
#     return True
# if __name__ == '__main__':
#     a =is_symmetrical('abcba')
#     print(a)
# a = '01 03 FA 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 50 41 '
#
# b = a.replace(' ','')
# print(b)
# a = 'abcddddddddddddddd'
# b = 'abcddddddddddddddd'
# c = b
# print(id(a),id(c))
# print(a is c)
# print(a ==c)
def fun_binary_search(ts,t):
    """ t:目标元素，
 		ts: 表示寻找范围的数组
        return ： 返回下标
    """
    height= len(ts) -1 # 因为是返回下标，所以要减一，不然会始终多1
    low = 0
    while low <= height: #某些情况下 他们相等也要做判断
        mid = (low + height) // 2
        if ts[mid] == t:
            return mid
        elif ts[mid] > t: # 说明我们找的范围大了，要去小的范围找
            height = mid - 1
        else:
            low = mid + 1
    return None

def fun2_binary_search(ts, t):
    """
    递归的方法就是要 改变ts的范围实现查找
    t:目标元素
    ts:表示寻找范围的数组
    return ： 返回下标
    """
    low = 0
    height = len(ts) - 1
    mid = (low + height) // 2
    if ts[mid] == t:
        return True
    elif ts[mid] > t:
        return fun2_binary_search(ts[:mid], t)
    else:
        return fun2_binary_search(ts[mid + 1:],t)

def fun3_binary_search(ts,t,low,height):
    '''

    :param ts:  数组
    :param t:   目标值
    :param low:  下标最小值
    :param height: 下标最大值
    :return:
    '''
    if height == 0:
        return False
    else:
        if low <=height:
            mid = (low+height) //2
            if ts[mid] == t:
                return mid
            elif ts[mid] > t:
                return fun3_binary_search(ts,t,low,height=mid-1)
            else:
                return fun3_binary_search(ts,t,low=mid+1,height=height)

def fun4_binary_search(ts,t):
    '''
    使用内嵌的方式，将传参隐藏
    :param ts: 数组
    :param t:目标值
    :return: 下标
    '''
    def inner_func(low,height):
        if low <= height:
            mid = (low + height) // 2
            if ts[mid] == t:
                return mid
            elif ts[mid] < t: # 寻找的元素小了，那要把最小值提高
                return inner_func(low=mid+1,height = height)
            else:
                return inner_func(low=low,height=mid-1)
        return False
    return inner_func(0,len(ts)-1)
if __name__ == '__main__':
    ts = [1,2,4,5,6,7]
    print(fun4_binary_search(ts,4))
    # print(binary_search(ts,3,0,len(ts)-1))
    # print(binary_search(ts, 4,0,len(ts)-1))
    # print(binary_search(ts, 5,0,len(ts)-1))
    # print(binary_search(ts, 6,0,len(ts)-1))
    # print(binary_search(ts, 7))
    # print(my_dg(4,ts))
    # print(my_dg(5, ts))
    # print(my_dg(6, ts))
    # print(my_dg(7, ts))
    # print(fun3_binary_serarch(ts,2,0,len(ts)-1))
    # print(fun3_binary_serarch(ts, 4,0,len(ts)-1))
    # print(fun3_binary_serarch(ts, 5,0,len(ts)-1))
    # print(fun3_binary_serarch(ts, 6,0,len(ts)-1))
    # print(fun3_binary_serarch(ts, 7,0,len(ts)-1))
    # print(fun3_binary_serarch(ts, 8,0,len(ts)-1))
    # print(fun(ts,2,0,len(ts)-1))
    # print(fun(ts, 3, 0, len(ts) - 1))
    # print(fun(ts, 4, 0, len(ts) - 1))
    # print(fun(ts, 5, 0, len(ts) - 1))
    # print(fun(ts, 6, 0, len(ts) - 1))
    # print(fun_binary_search(2,ts))