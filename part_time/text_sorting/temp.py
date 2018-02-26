'''
20180125 LIRUI
'''
import chardet
import copy
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
    for i in range(len(arr)-2):
        #print(arr[i])
        temp = []
        temp.append(arr[i])
        temp.append(arr[i+1])
        temp.append(arr[i+1+1])
        #print(temp)
        sample = ["1","."," "]
        if temp == sample:

            arr[i] = copy.deepcopy(num)
            print(arr[i])
            num += 1

    return num

#文字の切り替え
def delete(arr):

    text1 = arr.replace("[", "")
    text1 = text1.replace("]", "")
    text1 = text1.replace("<sup>", "")
    text1 = text1.replace("</sup>", "")

    return text1


#TXTファイルを読み込み、encodingを注意
with open("test1.txt", "r", encoding="UTF-8") as f:
    text = f.read()



text1 = delete(text)
#tolist
text2 = list(text1)
print(type(text2))
num = convert(text2)
print("the number of 1:", num, end="\n\n")

#output
print ("Sample output loading.......")



print(text1)

#testsuite
temp = "年以降を選択"
my_str_as_bytes = str.encode(temp)
print(my_str_as_bytes)
print(chardet.detect(my_str_as_bytes))