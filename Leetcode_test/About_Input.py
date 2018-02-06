#强转数据类型
n = int(input())
#Python的sqlit（）函数：最基本用法：str.split(sep=None, maxsplit=-1)
#Example：
#数据类型会发生变化
name_numbers1 = input()
name_numbers2 = name_numbers1.split()
print(type(name_numbers1))
print(type(name_numbers2))