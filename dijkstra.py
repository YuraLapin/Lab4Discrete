import matrix_functions
import consts

def get_neighbours(matrix, index):
    size = len(matrix)
    resulting_list = []
    for i in range(size):
        if matrix[index][i] != 0:
            resulting_list.append((i, matrix[index][i]))
    return resulting_list

def matrix_sum(matrix):
    ans = 0
    for arr in matrix:
        for elem in arr:
            ans += elem
    ans += 1
    return ans

def get_minimal_not_confirmed(distantions, confirmed, infinity):
    size = len(distantions)
    min = infinity
    min_id = -1
    for i in range(size):
        if i not in confirmed:
            if distantions[i] < min:
                min = distantions[i]
                min_id = i
    return min_id

def get_prevs(matrix, index):
    size = len(matrix)
    resulting_list = []
    for i in range(size):
        if matrix[i][index] != 0:
            resulting_list.append((i, matrix[i][index]))
    return resulting_list

def count_roads(matrix):
    ans = 0
    for arr in matrix:
        for elem in arr:
            if elem != 0:
                ans += 1
    return ans

def check_path(matrix, start_index, finish_index):
    one_matrix = matrix_functions.set_to_ones(matrix)
    for i in range(count_roads(one_matrix) + 1):
        if matrix_functions.rise_matrix_to_power(one_matrix, i)[start_index][finish_index] != 0:
            return True
    return False

def find_path(matrix, start_index, finish_index):
    if matrix_functions.check_matrix(matrix):
        if check_path(matrix, start_index, finish_index):
            confirmed = []
            infinity = matrix_sum(matrix)
            distantions = [infinity for i in matrix]
            distantions[start_index] = 0

            neighbours = get_neighbours(matrix, start_index)
            for elem in neighbours:
                distantions[elem[0]] = min(distantions[elem[0]], elem[1])
            confirmed.append(start_index)

            while infinity in distantions or finish_index not in confirmed:
                current = get_minimal_not_confirmed(distantions, confirmed, infinity)
                neighbours = get_neighbours(matrix, current)
                for elem in neighbours:
                    distantions[elem[0]] = min(distantions[elem[0]], elem[1] + distantions[current])
                confirmed.append(current)

            print(consts.LINE)
            print("Расстояния до вершин:")
            print(distantions)

            route = [finish_index]
            while start_index not in route:
                current = route[len(route) - 1]
                for elem in get_prevs(matrix, current):
                    if distantions[elem[0]] + elem[1] == distantions[current]:
                        route.append(elem[0])
                        break

            for i in range(len(route)):
                route[i] += 1

            print("Маршрут:")
            route.reverse()
            print(route)
        
        else:
            print(consts.LINE)
            print("Маршрута не существует")