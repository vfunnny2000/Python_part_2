# Напишите функцию для транспонирования матрицы

MATRIX = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
]


def main():
    print("Your matrix:")
    print_matrix(MATRIX)
    print("Transposed matrix:")
    print_matrix(transpose_matrix(MATRIX))


def print_matrix(matrix: list[list]):
    # """Вывод квадратной матрицы на экран"""
    for row in matrix:
        print(row)


def transpose_matrix(matrix: list[list]) -> list[list]:
    # """Транспонирование матрицы"""
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix


if __name__ == "__main__":
    main()


# **********************************************************************************

# def transpose_matrix(matrix):
#     return list(map(list, zip(*matrix)))


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# transposed_matrix = transpose_matrix(matrix)
# print(transposed_matrix)

# ***************************************************************************************

# def transpose_matrix(matrix):
#     return [list(row) for row in zip(*matrix)]


# matrix = [[1, 2, 3],
#           [4, 5, 6]]

# transposed = transpose_matrix(matrix)
# print(transposed)




# def transpose(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0

#     transposed = [[0 for _ in range(rows)] for _ in range(cols)]

#     for i in range(rows):
#         for j in range(cols):
#             transposed[j][i] = matrix[i][j]

#     return transposed


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# print(transposed_matrix)