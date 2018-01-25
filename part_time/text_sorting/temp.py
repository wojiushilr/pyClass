import pandas as pd
import numpy as np
import chardet
from wordcloud import WordCloud
import matplotlib.pyplot as plt
'''
#v1
text_sample = pd.read_csv('textSample.txt', encoding= "ShiftJIS", sep="delimiter",error_bad_lines=False, engine='python')
text_sample = np.array(text_sample)

#text_out = text_sample.decode('unicode_escape')

print(text_sample)
'''
#数字”１”を削除
def convert(arr):

    num = 0

    for i in range(len(arr)):

        if arr[i] == "1":
            num += 1

    return num

#TXTファイルを読み込み、encodingを注意
with open("test1.txt", "r", encoding="UTF-8") as f:
    text = f.read()

#文字の切り替え
text1 = text.replace("[論文PDF]", "")

#output
print (type(text1))

text2 = list(text1)

print(len(text2))

num = convert(text1)
print(num)

#testsuite
temp = "年以降を選択"
my_str_as_bytes = str.encode(temp)
print(my_str_as_bytes)
print(chardet.detect(my_str_as_bytes))