import user_inputs
import consts
import matrix_functions
import components
import spf

def main():
	size = user_inputs.get_positive_int("Введите размер матрицы: ")
	matrix = matrix_functions.fill_matrix_with_zero(size)

	go_on = True
	while go_on:
		print(consts.LINE)
		matrix_functions.print_matrix(matrix)
		print(consts.LINE)
		print("1 - Добавить связь")
		print("2 - Удалить связь")
		print("3 - Найти компоненты связности")
		print("4 - Построить ярусно-параллельную форму")
		print("5 - Построить клику")
		print("6 - Построить маршрут из точки A в точку B алгоритмом Дейкстры")
		print("7 - Выход")
		ans = user_inputs.get_int("Выберите действие [1-3]: ")
		if ans == 1:
			n_1 = user_inputs.get_positive_int_lower_than("Введите номер вершины отправления: ", size)
			n_2 = user_inputs.get_positive_int_lower_than("Введите номер вершины прибытия: ", size)
			weight = user_inputs.get_positive_int("Введите вес ребра: ")
			matrix[n_1 - 1][n_2 - 1] = weight	
		elif ans == 2:
			n_1 = user_inputs.get_positive_int_lower_than("Введите номер вершины отправления: ", size)
			n_2 = user_inputs.get_positive_int_lower_than("Введите номер вершины прибытия: ", size)
			matrix[n_1 - 1][n_2 - 1] = 0		
		elif ans == 3:
			components.find_components(matrix)
		elif ans == 4:
			spf.find_spf(matrix)
		elif ans == 5:
			print("ERROR")
		elif ans == 6:
			n_1 = user_inputs.get_positive_int_lower_than("Введите номер вершины отправления: ", size)
			n_2 = user_inputs.get_positive_int_lower_than("Введите номер вершины прибытия: ", size)
			print("ERROR")
		elif ans == 7:
			go_on = False
		else:
			print("Введено неверное число")
		
if __name__ == "__main__":
	main()	