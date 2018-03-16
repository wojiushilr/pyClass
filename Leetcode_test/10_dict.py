

n = int(input())
name_numbers = [input().split(" ") for _ in range(n)]
print(name_numbers[0][0])
#[['sam', '111']]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break

l = 'sam 111'
print(l.split())


a=" \rzha ng\n\t "
print(a.split())


str = "*****this is string example....wow!!!*****"
print (str.strip( '*' ))

str = "this is string example....wow!!!"
print (str.split( ))
print (str.split('i',1))
print (str.split('w'))
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。


