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


#v2
with open("textSample.txt", "r",encoding="UTF-8") as f:
    text = f.read()


#type = chardet.detect(text)
text1 = text.strip(" ")
#text2 = "".join(text1)
print (text1)
#print (text1)
#print (text2)


temp = "年以降を選択"
print(temp.encode("utf-8"))