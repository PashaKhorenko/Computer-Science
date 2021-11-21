prodolship = 'Z'
while prodolship == 'Z':
	x = float(input("Введите первое число: "))
	correct_sing = False
	while not correct_sing:
		sing = input("Укажите знак опепации +, -, *, /: ")
		if sing == '+' or sing == '-' or sing == '*' or sing == '/':
			correct_sing = True
		else:
			print("Не правильно введённый знак. Попрубуйте ещё раз.")
	y = float(input("Введите второе число: "))
	if sing == '+':
		print(x+y)
	elif sing == '-':
		print(x-y)
	elif sing == '*':
		print(x*y)
	else:
		if y != 0:
			print(x/y)
		else:
			print("!!! ERROR !!!")
			correct_sing = False

	oper = str(input("Желаете продолжить? Есла желаете напишите '+', а если нет - любую клавишу: "))
	if oper == '+':
		correct_sing = False
	else:
		break
