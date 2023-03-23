import user_inputs
import consts
import matrix_functions
import components
import spf
import dijkstra
import clique

def main():
	size = user_inputs.get_positive_int("Введите размер матрицы: ")
	matrix = matrix_functions.fill_matrix_with_zero(size)
	#matrix = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0]]

	go_on = True
	while go_on:
		print(consts.LINE)
		matrix_functions.print_matrix(matrix)
		print(consts.LINE)
		print("1 - Добавить связь")
		print("2 - Удалить связь")
		print("3 - Заново заполнить матрицу")
		print("4 - Найти компоненты связности")
		print("5 - Построить ярусно-параллельную форму")
		print("6 - Построить маршрут из точки A в точку B алгоритмом Дейкстры")
		print("7 - Построить клику")
		print("8 - Выход")
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
			print(consts.LINE)
			print("Введите " + str(size) + " строчек целых чисел, разделяя их пробелами: ")
			matrix = user_inputs.enter_matrix(size)	
		elif ans == 4:
			components.find_components(matrix)
		elif ans == 5:
			spf.find_spf(matrix)
		elif ans == 6:
			print(consts.LINE)
			n_1 = user_inputs.get_positive_int_lower_than("Введите номер вершины отправления: ", size)
			n_2 = user_inputs.get_positive_int_lower_than("Введите номер вершины прибытия: ", size)
			dijkstra.find_path(matrix, n_1 - 1, n_2 - 1)
		elif ans == 7:
			print(consts.LINE)
			clique_size = user_inputs.get_positive_int("Введите длину клики для поиска: ")
			clique.find_cliques(matrix, clique_size)
		elif ans == 8:
			go_on = False
		else:
			print("Введено неверное число")
		
if __name__ == "__main__":
	main()	