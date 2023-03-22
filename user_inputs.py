def check_int(str):
	if str == None or str == "":
		return False
	for char in str:
		if char not in "-0123456789":
			return False
	return True

def get_int(message):
	print(message)
	ans = input()
	while not check_int(ans):
		print("Число должно состоять только из цифр и быть целым")
		print(message)
		ans = input()
	return int(ans)

def get_positive_int(message):
	ans = get_int(message)
	while ans <= 0:		
		print("Число должно быть положительным ")
		ans = get_int(message)		
	return ans	

def get_positive_int_lower_than(message, max):
	ans = get_positive_int(message)
	while ans > max:		
		print("Число не может быть больше ", max)
		ans = get_positive_int(message)		
	return ans	

def check_if_list_is_int(list_to_check):
	for elem in list_to_check:
		if not check_int(elem):
			return False
	return True

def get_list(size):
	user_input = input()
	while len(user_input.split(" ")) != size or not check_if_list_is_int(user_input.split(" ")):
		print("Строка должна состоять из " + str(size) + " целых чисел")
		user_input = input()
	return user_input

def enter_matrix(size):
	matrix = []
	for i in range(size):
		current_line = []
		user_input = get_list(size)
		for elem in user_input.split(" "):
			current_line.append(int(elem))
		matrix.append(current_line)
	return matrix