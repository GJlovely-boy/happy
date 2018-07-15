# -*- coding:utf-8 -*-
# 读入用户输入的字符串，分别统计字符串中大写字母，小写字母，字母的个数

str1  = input("请输入一个字符串:")
i = 0 
num1 = 0
num2 = 0
num3 = 0
while i < len(str1):
	if 97 <= ord(str1[i]) <= 122:
		num1 += 1
	elif 65 <= ord(str1[i]) <= 90:
		num2 += 1
	elif 48 <= ord(str1[i]) <= 57:
		num3 += 1
	i += 1
print("小写字母个数 = {},\n大写字母个数={},\n数字个数={}".format(num1,num2,num3))
