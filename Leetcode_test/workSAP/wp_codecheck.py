# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:10:44 2018

@author: LuMH
"""



import sys
#s = input()
s = '6 4'
N = int(s.split()[0])
K = int(s.split()[-1])
#S = input()
S = 'AABBAA'

sd = {}
#for i in range(K):
#    s = input()
#    m = s.split()[0]
#    v = int(s.split()[-1])
#    sd[m] = v

#spell = ["A 1", "AA 3", "C 1", "CBA 14", "BA 5", "BC 4", "CC 3", "CA 4", "ABC 6", "ACCB 14", "AB 2", "BAB 9", "BBA 13"]


def myfind(S_find, s_find):
    idx = []
    for i in range(len(S_find)):
        idx_temp = S_find.find(s_find, i)
        if idx_temp not in idx and idx_temp != -1:
            idx.append(idx_temp)
    return idx
    
def myreplace(S_find, s_find, idx):
    S_temp = S_find[idx:]
    S_temp = S_temp.replace(s_find,'', 1)
    #print("s_temp",S_temp)
    S_temp = S_find[:idx] + S_temp
    return S_temp

spell = ['BB 1', 'AA 1', 'AB 3', 'AAAA 4']
for s in spell:
    m = s.split()[0]
    v = int(s.split()[-1])
    sd[m] = v
print("sd",sd)


sub_s = [S]
f = {}
loc = {}
spelled = {}
for m,v in sd.items():
    f[m] = [v]
    loc[m] = [-1]
    spelled[m] = [0]

print("\n")
print("sub_s",sub_s)
print("f",f)
print("loc", loc)
print("spelled", spelled)
print("\n")

#求子集

for s in sub_s:
    #print(s)
    #print(sub_s)
    #print(f)
    #print("\n\n")
    if s not in f:
        f[s] = []
        loc[s] = []
        spelled[s] = []
    flag = False
    for m in sd:
        if m in s:
            flag = True
            location = myfind(s, m)
            print("location",location)
            for i in location:
                print("s",s)
                print("m",m)
                print("i",i)
                temp_s = myreplace(s, m, i)
                print("temp_s",temp_s)
                if temp_s != '':
                    f[s].append(temp_s)
                    if temp_s not in sub_s:
                        sub_s.append(temp_s)
                    loc[s].append(i)
                    spelled[s].append(m)
    if flag == False:
        f[temp_s] = [0]
        loc[temp_s] = [-1]
        spelled[temp_s] = [0]

#print("spelled2",spelled,end="\n")

value = {}
print("\n")
print("sub_s_0", sub_s )
sub_s.reverse()
print("sub_s",sub_s)
for s in sub_s:
    value[s] = []
    for i in range(len(f[s])):
        print("s","i",s,i)
        print("spelled",spelled)
        print("spelled[s][i]",spelled[s][i])
        if spelled[s][i] == 0:
            value[s].append(f[s][i] + spelled[s][i])
#            f[s][i] = f[s][i] + spelled[s][i]
        else:
            value[s].append(max(value[f[s][i]]) + value[spelled[s][i]][0])
#            f[s][i] = max(f[f[s][i]]) + f[spelled[s][i]][0]

opt_value = max(value[S])
while isinstance(S, str):
    idx = value[S].index(max(value[S]))
    if loc[S][idx] != -1:
        sys.stdout.write(str(loc[S][idx]) + ' ' + spelled[S][idx] + '\n')
    else:
        sys.stdout.write(str(0) + ' ' + S + '\n')
    S = f[S][idx]

sys.stdout.write(str(opt_value) + '\n')
