# -*- codind:UTF-8 -*-
# 读入用户输入的两个整形数，判断其大小关系
num1 = int(input('请输入第一个整形数:'))
num2 = int(input('请输入第二个整形数:'))
if num1 < num2:
	print("{}小于{}".format(num1,num2))
elif num1 == num2:
	print("{}等于{}".format(num1,num2))
else:
	print("{}大于{}".format(num1,num2))
