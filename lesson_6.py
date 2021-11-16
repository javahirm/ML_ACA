class Matrix(object):
    def __init__(self, *args, **kwargs):
        """
        if filename given => read from file
        if list => just read it
        """

        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self._matrix = kwargs['list']
        # self._columns =
        # self._rows =

    def read_as_list(self, matrix_list):
        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')
        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        """
        Read from file and store
        """

        file = open("matrix_example.txt", "r")
        lines = file.read().splitlines()
        file.close()
        the_matrix = []
        # if len(lines) == 0:
        #     raise ValueError("Got empty matrix")
        for line in lines:
            line = line.split()
            the_matrix.append(line)

        def str_to_float(num):
            new_list = []
            for elem in num:
                elem = float(elem)
                new_list.append(elem)
            return new_list

        new_matrix = list(map(str_to_float, the_matrix))
        return new_matrix

    def __str__(self):
        s = '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'columns - {self.shape[0]}\nrows = {self.shape[1]}'
        return s

    def write_to_file(self, filename):
        """
        Write to file
        """
        file = open("written_matrix.txt", "w+")
        file.write()
        file.close()
    def transpose(self):
        pass

    def shape(self):
        return self._rows, self._columns

    def __add__(self, other):  # +
        pass

    def __mul__(self, other):  # *
        pass

    def __matmul__(self, other):  # @
        pass

matrix_a = Matrix()
# matrix_b = Matrix()
# # print(a * b)
#
#
# a = matrix_a.read_from_file("matrix_example.txt")
# print(a)

m = Matrix(filename = "matrix_example.txt")
print(m.read_from_file())
