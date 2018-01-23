'''
def isPalindrome(s):
    if len(s) < 2: #如果字符串只有0个或1个字符，那么该字符串符合回文的定义
        return True
    if s[0]!=s[-1]: #如果字符串不止一个字符，那么检查字串符的第一项和最后一项是否等同
        return False
    return isPalindrome(s[1:-1]) #字串符的第一项和最后一项等同，所以去除字符串的第一项和最后一项，继续进行检查

str=input("请输入一个字符串： ")
if isPalindrome(str):
    print(str+"是一个回文字符串")
else:
    print(str+"不是一个回文字符串")


'''

import  sys


a=input('your enter:\n')
b = []
c = []
s= 0

[c.append(i) for i in a if not i in c]
print(c)


for n in range(len(a)-1):
    for i in range(0,len(a) ):
        m=a[len(a) -i-1]
        b.append(m)

    for j in range(len(a) ):
       mark=True
       if a[j]!=b[j]:
           mark=False

    if mark == False:
        break

    a = a[1:-1]
    print("changdu" , len(a))

    s += 1
    print("s" , s)




print(s+len(c))

