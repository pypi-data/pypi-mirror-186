import numpy as np


class DistanceMatrix:
    def __init__(self, n_cells):

        self.D = np.zeros([n_cells, n_cells])
        self.n_cells = n_cells

    def __call__(self, X):

        for i in range(self.n_cells):
            cell = X[i, :]
            X_tiled = np.tile(
                cell[None, :], reps=(self.n_cells, 1)
            )  # one cell x n_cells
            # distance between that cell and all other cells, summed over all 50 PCs / dims
            self.D[i, :] = np.sqrt(np.sum(np.square(X_tiled - X), axis=1))

        return self.D


def compute_distance_matrix(adata, use_key="X_pca"):

    n_cells = adata.shape[0]

    distance_matrix = DistanceMatrix(n_cells)
    adata.obsp["X_dist"] = distance_matrix(X=adata.obsm[use_key])