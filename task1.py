# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transposed.append(transposed_row)
    return transposed


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = transpose(matrix)
print(result)
