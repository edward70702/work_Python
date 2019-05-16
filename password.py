x = 0
while x < 3 :
	password =  input('請輸入你的密碼: ') 
	if password == 'a123456':
		print('輸入正確,已登入')
		break
	else:
		print('輸入錯誤，請重新輸入，還剩',2-x,"次")
		x = x + 1
		if x == 3:
			print('已退出。請重新執行程式')