def get_matrix(n, m, value):
    matrix = []
    if m <= 0:
        return matrix
    for i in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[i].append(value)
    return matrix


print(get_matrix(4, 2, 4))
print(get_matrix(5, 3, 2))
print(get_matrix(4, 5, 8))
print(get_matrix(-1, -1, 3))
print(get_matrix(-1, 2, 3))
print(get_matrix(3, -1, 3))
