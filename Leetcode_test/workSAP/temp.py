S = 'AABBAAAAA'
sd = {'BB': 1, 'AA': 1, 'AB': 3, 'AAAA': 4}
sub_s = [S]
sd2 = ["BB","AA","AB","AAAA"]
sd3 ={'BB': [0], 'AA': [0], 'AB': [0], 'AAAA': [0, 'AA', 'AA', 'AA'],
      'AABBAA': ['BB', 'AA', 'AA', 'AB'], 'BBAA': ['BB', 'AA'], 'AABB':
          ['BB', 'AA', 'AB'], 'ABAA': ['AA', 'AB']}

print(sub_s)
for s in sub_s:
    print(s)
print("sd",sd)


print("\nverity of 字典遍历")
for m,v in sd.items() :
    print(m)
    print(v)


print("\nverify of python判断字符串（string）是否包含（contains）子字符串的方法")
for m in sd:
    if m in s:
        print("S",s)
        print("m",m)


def myfind(S_find, s_find):
    idx = []
    print("\nverify of function myfind")
    print("S_find",S_find)
    print("s_find",s_find)
    for i in range(len(S_find)):
        print("i",i)
        idx_temp = S_find.find(s_find, i)
        print("idx_temp",idx_temp)
        if idx_temp not in idx and idx_temp != -1:
            idx.append(idx_temp)
    return idx

result = myfind(s,"BB")
print("idx",result)


print("sd3['AAAA'][1]",sd3["AAAA"][1])