def check_matrix(matrix):
	outerLength = len(matrix)
	for arr in matrix:
		if outerLength != len(arr):
			return False
	return True

def print_matrix_element(num, matrix_size):
	spaces = len(str(matrix_size)) - len(str(num)) + 1
	print(num, end = spaces * " ")

def print_matrix(matrix):
	if check_matrix(matrix):
		size = len(matrix)
		for i in range(size + 1):
			print_matrix_element(i, size)
		print()
		for i in range(size):
			print_matrix_element(i + 1, size)
			for j in range(size):
				print_matrix_element(matrix[i][j], size)
			print()
			
def fill_matrix_with_zero(size):
	ans = [[0 for i in range(size)] for j in range(size)]
	return ans

def multiply_matrix(matrix_1, matrix_2):
	size = len(matrix_1)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
			size = len(matrix_1)
			for i in range(size):
				for j in range(size):
					for k in range(size):
						ans[i][j] += matrix_1[k][j] * matrix_2[i][k]
					ans[i][j] = min(1, ans[i][j])
	return ans

def rise_matrix_to_power(matrix, power):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix):
		if power == 0:
			for i in range(size):
				ans[i][i] = 1
		elif power == 1:
			ans = matrix	
		elif power > 1:
			ans = matrix
			for i in range(power - 1):
				ans = multiply_matrix(ans, matrix)
	return ans

def sum_matrix(matrix_1, matrix_2):
	size = len(matrix_1)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix_1[i][j] + matrix_2[i][j]
				ans[i][j] = min(1, ans[i][j])
	return ans

def sum_of_line_of_matrix(matrix, count):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	for i in range(count + 1):
		ans = sum_matrix(ans, rise_matrix_to_power(matrix, i))
	return ans

def transpose(matrix):
	size = len(matrix)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix[j][i]
	return ans

def logical_and(matrix_1, matrix_2):
	size = len(matrix_1)
	ans = fill_matrix_with_zero(size)
	if check_matrix(matrix_1) and check_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
		for i in range(size):
			for j in range(size):
				if matrix_1[i][j] == matrix_2[i][j] == 1:
					ans[i][j] = 1
				else:
					ans[i][j] = 0
	return ans