import numpy as np
from .._utilities import Base

class Laplacian(Base):
    def __init__(self, adata, adjacency_key="adjacency"):

        n_cells = adata.shape[0]
        A = adata.obsp[adjacency_key]

        self.__parse__(locals(), private=["adjacency_key", "n_cells"])

    def _configure_identity_matrix(self):
        if not hasattr(self, "_identity_matrix"):
            self._identity_matrix = np.identity(self._n_cells)

    @property
    def identity_matrix(self):
        self._configure_identity_matrix()
        return self._identity_matrix

    def row_sum_normalize(self, A):

        s = np.sum(A, axis=1)
        X, Y = np.meshgrid(s, s)
        return A / Y

    def __call__(self):
        return self.identity_matrix - self.row_sum_normalize(self.A)
    
def compute_Laplacian(adata, adjacency_key="adjacency", key_added="Laplacian"):
    
    L = Laplacian(adata)
    adata.obsp['Laplacian'] = L()