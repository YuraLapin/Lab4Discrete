import matrix_functions
import consts
import copy

def has_cycles(matrix):
	new_matrix = matrix_functions.set_to_ones(matrix)
	new_matrix = matrix_functions.rise_matrix_to_power(new_matrix, len(new_matrix) + 1)
	for arr in new_matrix:
		for elem in arr:
			if elem != 0:
				return True
	return False

def restore_position(num, previous_array):
	checked = []
	flag = True
	while flag:
		flag = False
		for arr in previous_array:
			for elem in arr:
				if elem not in checked:
					if elem <= num:
						checked.append(elem)
						num += 1
						flag = True
	return num

def get_spf(matrix, resulting_array):
	if matrix_functions.check_matrix(matrix):
		new_matrix = copy.deepcopy(matrix)
		size = len(new_matrix)
		current_level = []
		to_delete = []
		for i in range(size):
			only_nuls = True
			for j in range(size):
				if new_matrix[j][i] != 0:
					only_nuls = False
			if only_nuls:
				to_delete.append(i)
				current_level.append(restore_position(i + 1, resulting_array))
		resulting_array.append(current_level)
		to_delete.reverse()
		for index in to_delete:
			new_matrix.pop(index)
			for arr in new_matrix:
				arr.pop(index)
		if len(new_matrix) > 0:
			return get_spf(new_matrix, resulting_array)
		else:
			return resulting_array

def find_spf(matrix):
	if matrix_functions.check_matrix(matrix):
		print(consts.LINE)
		print("Ярусно-параллельная форма:")		
		if has_cycles(matrix):
			print("ЯПФ не может быть получена, так как в графе есть цикл")
		else:
			print(get_spf(matrix, []))