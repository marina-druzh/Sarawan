class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        # дабы разобраться и плохо зная синтаксис сделаем по шагам
        b = str()
        for row in self.matrix:
            a = str()
            for i in list(row):
                a += str(i) + ' '
            b += str(a) + '\n'
        return b
        # return '\n'.join(' '.join([str(i) for i in row]) for row in self.matrix) можно было так

    def __mul__(self, other):
        t = 0
        s = []
        c = []
        str_m = len(other.matrix)
        col_m = len(self.matrix[0])
        if str_m != col_m:
            return (f'Число столбцов первой матрицы должно совпадать с числом столбцов второй')
        try:
            for row in range(len(self.matrix)):
                for i in range(len(other.matrix[0])):
                    for j in range(len(self.matrix[0])):
                        t = t + int(self.matrix[row][j]) * int(other.matrix[j][i])
                    s.append(t)
                    t = 0
                c.append(s)
                s = []
            return Matrix(c)
        except IndexError:
            return f'Ошибка размерностей матриц!'


m_1 = [[1, 1], [1, 1], [1, 1], [1, 1]]
m_2 = [[1, 1, 1, 1], [1, 1, 1, 1]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 * mtrx_2

print(mtrx_1, end='')
print('-' * 30)
print(mtrx_2, end='')
print('-' * 30)
print(f'Mult_m:\n{new_m}')


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 * mtrx_2

print(mtrx_1, end='')
print('-' * 30)
print(mtrx_2, end='')
print('-' * 30)
print(f'Mult_m:\n{new_m}')