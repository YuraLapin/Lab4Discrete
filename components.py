import matrix_functions
import consts
import copy

def count(list):
	ans = 0
	for arr in list:
		for elem in arr:
			ans += 1
	return ans

def get_components(matrix, resulting_array):
	if matrix_functions.check_matrix(matrix):
		new_matrix = copy.deepcopy(matrix)
		size = len(new_matrix)
		current_component = []
		to_delete = []
		for i in range(size):
			if new_matrix[0][i] == 1:
				current_component.append(i + 1 + count(resulting_array))
				to_delete.append(i)
		to_delete.reverse()
		for index in to_delete:
			new_matrix.pop(index)
			for arr in new_matrix:
				arr.pop(index)
		resulting_array.append(current_component)		
		if len(new_matrix) > 0:
			return get_components(new_matrix, resulting_array)
		else:
			return resulting_array
		
def find_components(matrix):
	if matrix_functions.check_matrix(matrix):
		size = len(matrix)
		print(consts.LINE, "\nR:")
		r = matrix_functions.sum_of_line_of_matrix(matrix, size)
		matrix_functions.print_matrix(r)

		print(consts.LINE, "\nR^T:")
		r_t = matrix_functions.transpose(r)
		matrix_functions.print_matrix(r_t)

		print(consts.LINE, "\nR&R^T")
		answer = matrix_functions.logical_and(r, r_t)
		matrix_functions.print_matrix(answer)

		print(consts.LINE, "\nANSWER:")
		print(get_components(answer, []))