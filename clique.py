import matrix_functions
import consts

def check_if_oriented(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                return True
    return False

def check_if_clique(matrix, clique_list, index):
    for i in range(1, index):
        for j in range(i + 1, index):
            if matrix[clique_list[i] - 1][clique_list[j] - 1] == 0:
                return False
    return True

def print_clique(clique):
    for i in range(1, len(clique)):
        print(clique[i], end = " ")
    print()

def check_connection_count(matrix, index):
    ans = 0
    size = len(matrix)
    for i in range(size):
        if matrix[i][index] != 0:
            ans += 1
        if matrix[index][i] != 0:
            ans += 1
    return ans

def get_cliques(start_index, current_size, final_size, matrix, clique_list, degrees):
    size = len(matrix)
    for i in range(start_index + 1, size - (final_size - current_size) + 1):
        if degrees[i] >= (final_size - 1):
            clique_list[current_size] = i
            if check_if_clique(matrix, clique_list, current_size + 1):
                if (current_size < final_size):
                    get_cliques(i, current_size + 1, final_size, matrix, clique_list, degrees)
                else:
                    print_clique(clique_list)

def find_cliques(matrix, size):
    if matrix_functions.check_matrix(matrix):
        print(consts.LINE)
        if check_if_oriented(matrix):
            print("Граф должен быть неориентированным")
        else:
            clique_list = [0] * (size + 1)
            degrees = [0] * (len(matrix) + 1)
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] != 0:
                        degrees[i + 1] += 1
            print("Клики графа длиной " + str(size))
            get_cliques(0, 1, size, matrix, clique_list, degrees)