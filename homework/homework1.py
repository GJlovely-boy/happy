# 1.猜字游戏，随机产生10以内的整形数，可供用户猜，如果猜对，打印“ 厉害了”！500万属于你，如果猜错，如果比随机数大，提示“ 大了，再给你一次机会”，如果比随机数小，提示“  大胆一点”。用户最多有三次机会
'''
import random
i = 0
N = random.randint(1,10)
for i in range(0,3):
	N = eval(input("请输入10以内的整数:"))
	if N > n and i != 2:
		print("大了，再给你一次机会")
	elif N == n:
		print('厉害了！500万属于你')
		break
	elif N < n and i != 2:
		print('大胆一些')
	elif i == 2 and n != N: 
		print('game over')

'''
# 2.盒子里有3个红球，3个篮球，4个黄球，现要从盒子里拿出8个球，三个球有哪些分配情况

'''
cnt = 0
for r in range(0,4):
	for b in range(0,4):
		for y in range(0,5):
			if r + b + y == 8:
				cnt += 1
				print('红球{}篮球{}黄球{}'.format(r,b,y))
print("共{}种情况".format(cnt))
'''




# 3.打印 9 9 乘法表

'''
for i in range(1,10):
	for j in range(1,i+1):
		print("{} * {} = {:>2}".format(i,j,i*j),end= " ")
#		print("%d * %d = %d"%(i,j,i*j),end = ' ')
	print( )
'''
# 4.猴子得到一堆桃，当天吃了一半之后，又多吃了一个，以后每天，猴子都吃了剩余的一半桃子之后，又多吃一个，在第10天，只剩下1个桃子。输出这堆桃子最初有多少个
'''
num = 1
save = num
i = 0
for i in range(0,10):
	num = (num + 1)*2
	print(num)
'''
