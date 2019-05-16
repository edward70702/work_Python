import random

r = random.randint(1,10) ##先讓系統隨機建立一個數字
count = 0 #猜的次數

while True:
	x = input("猜數字遊戲!!請輸入1~10的整數: ") # X = 使用者輸入數字
	x = int(x)
	count += 1
	if x == r:
		print('\n答對了~~就是',r,'唷~~遊戲結束~~!!^O^~\n')
		break
	elif x < r :
		print('\n再大一點','你猜了',count,'次了~~\n')
	elif x > r :
		print('\n再小一點','你猜了',count,'次了~~\n')

