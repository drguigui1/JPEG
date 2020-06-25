# -*- coding: utf-8 -*-

import numpy as np

def zigzag(mat):
    '''
    Zigzag iteration over matrix 'mat'
    '''
    # init
    i, j, idx = 0, 0, 0
    n_rows, n_cols = mat.shape
    res = np.zeros(n_rows * n_cols)

    # first element case
    res[idx] = mat[i][j]
    idx += 1

    while (idx < n_rows * n_cols):
        if (j < n_cols -1):
            j += 1
        else:
            i += 1

        # diagonal from right to left
        while (j >= 0 and i < n_rows):
            res[idx] = mat[i][j]
            idx += 1
            i += 1
            j -= 1

        # out of bound i and j
        j += 1
        i -= 1

        if (i < n_rows - 1):
            i += 1
        else:
            j += 1

        # diagonal from left to right
        while (i >= 0 and j < n_cols):
            res[idx] = mat[i][j]
            idx += 1
            i -= 1
            j += 1

        # out of bound i and j
        i += 1
        j -= 1

    return res
