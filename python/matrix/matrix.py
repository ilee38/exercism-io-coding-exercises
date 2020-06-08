class Matrix:
    def __init__(self, matrix_string):
        self._rows = matrix_string.splitlines()

    def row(self, index):
        row = [int(val) for val in self._rows[index-1].split()]
        return row

    def column(self, index):
        column = []
        for i in range(1, len(self._rows)+1):
            row = self.row(i)
            column.append(row[index-1])
        return column

""" Alternate solution:

    class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(j) for j in i.split(' ')] for i in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [int(row[index-1]) for row in self.matrix]
"""