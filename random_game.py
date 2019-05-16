import random

count = 0 #猜的次數

y = input("\n猜數字遊戲!!請輸入要猜的區間~第一個數字: ") # X = 使用者輸入數字
z = input("\n請輸入要猜的區間~第二個數字: ")	
y = int(y)
z = int(z)

	

while y > z :
	print("\n第二個數字不能比較小啦 =皿=")
	y = input("\n重新輸入要猜的區間~第一個數字: ") # X = 使用者輸入數字
	z = input("\n輸入要猜的區間~第二個數字: ")	
	y = int(y)
	z = int(z)

r = random.randint(y,z) 

while True:
	
	x = input("開始猜吧~~請輸入數字: ")
	x = int(x)
	

	count += 1
	if x == r:
		print('\n答對了~~就是',r,'唷~~遊戲結束~~!!^O^~\n')
		
		break

	elif x < r :
		print('\n再大一點','你猜了',count,'次了~~\n')
	elif x > r :
		print('\n再小一點','你猜了',count,'次了~~\n')

