
import numpy as np


def row_sum_normalize(A):

        s = np.sum(A, axis=1)
        X, Y = np.meshgrid(s, s)
        return A / Y