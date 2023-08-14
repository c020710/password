password = 'a123456'
i = 3
while i > 0:
	x = input('Password: ')
	if x == password:
		print('Logged in succcessfully')
		break
	elif x != password:
		i = i - 1
		if i > 1:
			print(i, 'times remaining')
		elif i == 1:
			print('LAST CHANCE')
		else:
			print('ACCOUNT LOCKED')