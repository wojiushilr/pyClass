#!/bin/python3
'''
Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.:  or ), where  and .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM
Sample Output

19:05:45

'''
import sys
import time

def timeConversion(s):
    # Complete this function

    t = s.rstrip('APM').split(':')
    #print(type(t))
    t[0] = int(t[0])
    t[0] = t[0] % 12
    if 'PM' in s:
        t[0] += 12
        t[0] = str(t[0])
        time = ':'.join(map(str, t))
    elif 'AM' in s:

        t[0] = "0{0}".format(t[0]) #重点
        time = ':'.join(map(str, t))

    return time


s = input().strip()
result = timeConversion(s)
print(result)
