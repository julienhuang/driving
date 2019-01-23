#以年齡判斷可否開車
country = input('請問你是哪一國人? 台灣/美國')
age = int(input('請輸入你的年齡='))
if country == '台灣':
	if age >= 18:
		print('你可以考駕照!')
	else:
		print('你還不能考駕照喔~')
if country == '美國':
	if age >=16:
		print('你可以考駕照!')
	else:
		print('你還不能考駕照喔~')