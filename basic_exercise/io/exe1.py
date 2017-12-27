"exercise of python io"
"part one : input and re module"
import re
import numpy as np


#temp = int(input("Input the number:\n"))
#初始化一个空list，shape没有初始化
words = []
print("type of words", type(words))
print("first words", words)

#循环读取input数据
#使用re去除空格元素，把元素加入words
for i in range(3):
 inputWord = input("Input the words:\n")
 inputWord= re.sub(" ","",inputWord)
 print(inputWord)
 words.append(inputWord)



#l=re.split('[\. ]+',words)
print(len(words))
print("finally words", words)

"part two : Dictionary"
