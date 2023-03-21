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