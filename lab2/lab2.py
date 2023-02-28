import numpy as np


def div(matrix):
    file.write(str(matrix) + '\n') #вывод матрицы в файл
    original_matrix = matrix / matrix.max(axis = 1, keepdims = True) #деление на максимальный элемент
    np.set_printoptions(precision=3, floatmode='fixed') #округление
    file.write(str(original_matrix)) #вывод обработанной матрицы в файл


file = open("outout.txt", "w")
n = int(input())
m = int(input())
file.write(str(n) + ' ' + str(m) + '\n')
a = np.random.randint(0, 10, (m, n)) #автоматическая генерация матрицы
div(a)