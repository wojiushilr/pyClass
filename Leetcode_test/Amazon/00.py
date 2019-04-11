import sys
'''
def count(n, m, arr1, arr2):

    num = [0] * m  #number counting

    for i in range(m):
        for j in range(n):
          if  arr2[i] ==  arr1[j]:

              num[i] =num[i] + 1

    return num
'''
#
priceArrayA = []
priceArrayB = []
#
n = int(input().strip())
print(n)
for i in range(n)  :
   temp1 = input().strip()
   priceArrayA.append(temp1)

m = int(input().strip())
for j in range(m)  :
   temp2 = input().strip()
   priceArrayB.append(temp2)


print(priceArrayA)
print(priceArrayB)

#result = count(grades)
#print ("\n".join(map(str, result)))
#n = [0]*8
'''
num = count(n,m,arr1,arr2)
for i in num:

 print(i)

'''
