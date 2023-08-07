'''Class SVD'''
from random import randrange, random
import numpy as np
from SVD import SVD


def main():
    n = int(input("Число строк: "))
    m = int(input("Число столбцов: "))
    A = list(map(float, input('Введите набор чисел через пробел (количество чисел должны быть равно количеству строк умноденному на число столбцов): ').split()))
    A = np.array(A).reshape(n, m)
    #
    #x1 = randrange(1, 10)
    #x2 = randrange(1, 10)
    #A = np.array([[x1, x2], [x1 + x2, x1 + x2+random()], [x1 * x2, x1 * x2 + random()]])
    #print('[[x1, x2], [x1 + x2, x1 + x2+random()], [x1 * x2, x1 * x2 + random()]], x1, x2 - random')
    #print(A)
    #A = np.array([[1, 2], [3, 4], [7, 8]])
    svd = SVD(A)
    U, Sigma, V = svd.SVD()
    print("Матрица левых сингулярных векторов U \n", U)
    print("Sigma - аппроксимированная введенная матрица \n", Sigma)
    print("Матрица правых сингулярных векторов V - \n", V, "\n")
    print("Восстановленная матрица U*Sigma*V:\n", np.dot(U, np.dot(np.diag(Sigma), V)), "\n")


if __name__ == '__main__':
    main()
