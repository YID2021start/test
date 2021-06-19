x = 3
while True:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤剩餘次數' , x)
		x = x - 1
		if x == -1:
			print('帳戶已鎖定')
			break