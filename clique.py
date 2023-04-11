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

def check_list_insertion(outer_list, inner_list):
    answer = True
    for element in inner_list:
        if element not in outer_list:
            answer = False
    return answer

printed = []

def print_clique(clique):
    current_clique = []
    for i in range(1, len(clique)):
        current_clique.append(clique[i])

    already_printed = False
    for printed_clique in printed:
        if check_list_insertion(printed_clique, current_clique):
            already_printed = True

    if not already_printed:
        print(current_clique)
        printed.append(current_clique)

def check_connection_count(matrix, index):
    ans = 0
    size = len(matrix)
    for i in range(size):
        if matrix[i][index] != 0:
            ans += 1
        if matrix[index][i] != 0:
            ans += 1
    return ans

def clique_recursive(start_index, current_size, final_size, matrix, clique_list, degrees):
    size = len(matrix)
    for i in range(start_index + 1, size - (final_size - current_size) + 1):
        if degrees[i] >= (final_size - 1):
            clique_list[current_size] = i
            if check_if_clique(matrix, clique_list, current_size + 1):
                if (current_size < final_size):
                    clique_recursive(i, current_size + 1, final_size, matrix, clique_list, degrees)
                else:
                    print_clique(clique_list)

def find_cliques_by_size(matrix, size):
    clique_list = [0] * (size + 1)
    degrees = [0] * (len(matrix) + 1)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                degrees[i + 1] += 1
    clique_recursive(0, 1, size, matrix, clique_list, degrees)

def find_cliques(matrix):
    if matrix_functions.check_matrix(matrix):
        print(consts.LINE)
        if check_if_oriented(matrix):
            print("Граф должен быть неориентированным")
        else:
            size = len(matrix)
            i = size
            while i >= 2:
                find_cliques_by_size(matrix, i)
                i -= 1