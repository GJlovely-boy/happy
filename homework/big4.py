# -*- coding:utf-8 -*-
# 读入用户输入的字符串，按空格分割的每个字符串的首字母大写，其余都小写。
str1 = input("请输入一个字符串")
i =  0
str2 = str1.upper()
str3 = ''
while i < len(str2.split()):
	j = 1
	str3 =str3 + str2.split()[i][0]
	while j < len(str2.split()[i]):
		if 65 <= ord(str2.split()[i][j]) <=90:
			num1 =ord(str2.split()[i][j]) + 32
			str3 = str3 + chr(num1)
		else:
			str3 =str3 + chr(num1)
		j += 1
	str3 = str3 + ' '
	i += 1
print(str3)
