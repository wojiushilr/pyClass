import sys
import os


def countSpecialStrings(orderId):

    n = 1
    l = len(orderId)
    print(l,orderId)
    for i in range(l-1) :
        if l < 2:
            return True

        elif orderId[0] != orderId[-1]:
            print(orderId[0])
            return False
        else:
            orderId = orderId[1:-1]


str=input("请输入一个字符串： ")
if countSpecialStrings(str):
    print(str+"是一个回文字符串")
else:
    print(str+"不是一个回文字符串")