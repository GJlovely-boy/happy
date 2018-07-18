# -*- coding:utf-8 -*-
# 分别读入用户输入的两个字符串，比较其大小关系
#注意：字符串的大小跟长短无关，比较字符串中每一个字符的值，第一个不相等的字符的大小决定字符串大小。
str1 =input("请输入第一个字符串:")
str2 =input("请输入第二个字符串:")
i = 0
while True:
	if ord(str1[i]) > ord(str2[i]):
		print("{}大于{}".format(str1,str2))
		break
	elif ord(str1[i]) < ord(str2[i]):
		print("{}小于{}".format(str1,str2))
		break
	else:
		i += 1
		if i == len(str1) and i < len(str2):
			print("{}小于{}".format(str1,str2))
			break
		elif i < len(str1) and i == len (str2):
			print("{}大于{}".format(str1,str2))
			break
		elif i == len(str1) and i ==len(str2):
			print("{}等于{}".format(str1,str2))
			break
		
