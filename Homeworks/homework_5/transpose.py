def transposed(mat):
    rows = len(mat)
    columns = len(mat[0])
    transpose = []
    for _ in range(columns):
        new_rose = [None] * rows
        transpose.append(new_rose)
    for count, row in enumerate(mat):
        for i, value in enumerate(row):
            transpose[i][count] = value
    return transpose


matrix = [[1, 2, 3], [4, 5, 6]]
print(transposed(matrix))
