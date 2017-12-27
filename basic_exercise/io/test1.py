"exercise of python io"

import re
import numpy as np


temp = int(input("Input the number:\n"))

words = []
for i in range(6):
 inputWord = input("Input the words:\n")
 inputWord= re.sub(" ","",inputWord)
 if inputWord != None:
  words=words.append(inputWord)



l=re.split('[\. ]+',words)
print(len(words[0]))
print(l)
i=0

