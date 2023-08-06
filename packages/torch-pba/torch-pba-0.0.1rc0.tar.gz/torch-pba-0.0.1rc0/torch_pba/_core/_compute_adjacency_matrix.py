
import numpy as np

def compute_adjacency_matrix(adata, edges_key="edges"):

    edges = adata.uns[edges_key]

    i, j = edges[:, 0], edges[:, 1]
    N = np.max([i, j]) + 1
    A = np.zeros((N, N))
    A[i, j] = 1
    A[j, i] = 1
    
    adata.obsp['adjacency'] = A