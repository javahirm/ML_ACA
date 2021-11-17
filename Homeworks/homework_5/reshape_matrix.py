def reshape(matrix):
    all_elements = [number for elem in matrix for number in elem]
    rows_x_columns = len(matrix) * len(matrix[0])
    possible_inputs = [elem for elem in range(1, rows_x_columns + 1) if rows_x_columns % elem == 0]

    r = int(input("Rows of the reshaped matrix: "))
    c = int(input("Columns of the reshaped matrix: "))

    if r in possible_inputs and c in possible_inputs:
        reshaped_matrix = [all_elements[i:i + c] for i in range(0, rows_x_columns, c)]
        return reshaped_matrix
    else:
        return matrix


mat = [[1, 2, 3], [3, 4, 6], [5, 6, 9], [7, 8, 11]]
print(reshape(mat))
