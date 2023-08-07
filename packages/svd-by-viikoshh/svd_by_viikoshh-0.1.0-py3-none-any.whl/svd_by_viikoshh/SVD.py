import numpy as np
from math import log


class SVD:

    def __init__(self, A):
        self.A = A
        self.Sigma = None
        self.U = None
        self.V = None

    def SVD(self, A=None):

        def self_hstack(Arr1, Arr2):
            A1 = Arr1.tolist()
            A2 = Arr2.tolist()
            result = []
            for i in range(len(A1)):
                result.append([*A1[i], *A2[i]])
            return np.array(result)

        if A:
            self.A = A
        elif self.Sigma:
            return self.U[:, 1:], self.Sigma, self.V[:, 1:].T
        # вычисление ранга исходной матрицы A
        rank_A = np.linalg.matrix_rank(self.A)
        # инициализация переменных
        U = np.zeros((self.A.shape[0], 1))
        Sigma = []
        V = np.zeros((self.A.shape[1], 1))
        # вычисление количества итераций
        delta = 0.001  # (1 - delta) - вероятность получения точности epsilon
        epsilon = 0.01  # точность решения
        lambda_ = 2  # параметр, определяемый из неравенства min[i<j] (log(sigma_i /sigma_j))<=lambda
        iterations = int(log(4 * log(2 * self.A.shape[1] / delta) / (epsilon * delta)) /
                         (2 * lambda_))
        # старт степенного метода
        for _ in range(rank_A):
            u, sigma, v = self._one_component_svd(self.A, iterations)
            U = self_hstack(U, u)
            Sigma.append(sigma)
            V = self_hstack(V, v)
            self.A = self.A - u.dot(v.T.dot(sigma))
        # сохранение состояния для будущих вызовов
        self.U = U
        self.Sigma = Sigma
        self.V = V
        return U[:, 1:], Sigma, V[:, 1:].T

    def _one_component_svd(self, A, iters):
        def vect_norm(vect):
            return np.sum(np.abs(vect) ** 2) ** (1. / 2)

        math_expectation, standard_deviation = 0, 1
        x = np.random.normal(math_expectation, standard_deviation, size=A.shape[1])
        AtA = A.T.dot(A)
        for _ in range(iters):
            new_x = AtA.dot(x)
            x = new_x
        # определение одного вектора из матриц V, Sigma, U
        # v = x / np.linalg.norm(x)
        v = x / vect_norm(x)
        sigma = vect_norm(A.dot(v))
        u = A.dot(v) / sigma
        return np.reshape(u, (A.shape[0], 1)), \
            sigma, \
            np.reshape(v, (A.shape[1], 1))
