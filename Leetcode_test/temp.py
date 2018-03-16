'''

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

        print("Hello {0}".format(argv))


a = input()



main(a)
'''


# coding=gbk
# -*- coding: cp936 -*-
# 制作一个日历(只显示阳历日期）
'''实现方法：不使用python提供的calendar，根据给出的日期计算：
1.先根据输入年份得到这一年的第一天是星期几（(year + (year - 1)/4 - (year - 1)/100 + (year -1)/400)% 7）
2.再依据输入的日期（只需要年月就可以了）得到这个日期得到在当前年份的第几天
3.根据1和2得到当前月份的第一天是星期几。
4.创建日历，其实就是在5x7的表格中预先放置5*7个Label，分别表示1－31的情况（应该包含所有的情况）。
5.将1－31从得到的位置开始打印出来，以7为一行。
6.更新日历，当对日历头进行操作（改变日期时）就会更新日历显示的内容。
7.整个组件的布局是7x7的表格方式。第一行显示日历头，包括年月日的显示与选择；第二行为显示的日期，3-7为显示的月份信息。
'''


class Calendar:
    pass


AppCal = Calendar()
import time
from tkinter import *

def calcFirstDayOfMonth(year, month, day):
    '''计算某一日的是星期几'''
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 <= month <= 12:
        sum = months[month - 1]
    else:
        print('data error')
    # 对年月做了判断，日只是加了上下限，没有根据月判断输入的是否合法
    if year < 0 or month < 0 or month > 11 or day < 0 or day > 31:
        import os
        os._exit(1)

    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    # 先计算某年的第一天是星期几
    # (year + (year - 1)/4 - (year - 1)/100 + (year -1)/400)% 7
    return (sum % 7 - 1 + (year + (year - 1) / 4 - (year - 1) / 100 + (year - 1) / 400)) % 7


def createMonth(master):
    '''创建日历'''
    for i in range(5):
        for j in range(7):
            Label(master, text='').grid(row=i + 2, column=j)


def updateDate():
    ''' 更新日历'''
    # 得到当前选择的日期
    year = int(AppCal.vYear.get())
    month = int(AppCal.vMonth.get())
    day = int(AppCal.vDay.get())
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 判断是否瑞年
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        months[1] += 1
    fd = calcFirstDayOfMonth(year, month, 1)
    for i in range(5):
        for j in range(7):
            root.grid_slaves(i + 2, j)[0]['text'] = ''

    for i in range(1, months[month - 1] + 1):
        root.grid_slaves((i + fd - 1) / 7 + 2, (i + fd - 1) % 7)[0]['text'] = str(i)


def drawHeader(master):
    '''添加日历头'''
    # 得到当前的日期，设置为默认值
    now = time.localtime(time.time())
    col_idx = 0

    # 创建年份组件
    AppCal.vYear = StringVar()
    AppCal.vYear.set(now[0])
    Label(master, text='YEAR').grid(row=0, column=col_idx);
    col_idx += 1
    omYear = OptionMenu((master, AppCal.vYear) + tuple(range(2005, 2010)))
    omYear.grid(row=0, column=col_idx);
    col_idx += 1

    # 创建月份组件
    AppCal.vMonth = StringVar()
    AppCal.vMonth.set(now[1])
    Label(master, text='Month').grid(row=0, column=col_idx);
    col_idx += 1
    omMonth = OptionMenu((master, AppCal.vMonth) + tuple(range(1, 12)))
    omMonth.grid(row=0, column=col_idx);
    col_idx += 1

    # 创建年份组件
    AppCal.vDay = StringVar()
    AppCal.vDay.set(now[2])
    Label(master, text='DAY').grid(row=0, column=col_idx);
    col_idx += 1
    omDay = OptionMenu((master, AppCal.vDay) + tuple(range(1, 32)))
    omDay.grid(row=0, column=col_idx);
    col_idx += 1

    # 创建更新按钮
    btUpdate = Button(master, text='Update', command=updateDate)
    btUpdate.grid(row=0, column=col_idx);
    col_idx += 1

    # 打印星期标签
    weeks = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
    for week in weeks:
        Label(master, text=week).grid(row=1, column=weeks.index(week))


root = Tk()

drawHeader(root)
createMonth(root)
updateDate()

root.mainloop()