#!/usr/bin/python
# -*- coding: UTF-8 -*-
#http://www.runoob.com/python/python-object.html
class Employee:
    '所有员工的基类'
    empCount = 0
    #第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    #self 后面的属性命名随意
    def __init__(self, AAAAA,BBBBB ):
        self.name = AAAAA
        self.salary = BBBBB
        #empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


line = ["aasdasdas"]
temp = ["<br>"]
for i in line+temp:
 print(i, end="")