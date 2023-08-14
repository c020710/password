password = 'a123456'
i = 3
while i > 0:
	x = input('Password: ')
	if x == password:
		print('Logged in succcessfully')
		break
	else:
		i = i - 1
		print(i, 'times remaining')