
import numpy as np
import pandas as pd
from autodevice import AutoDevice
import torch


from .._utilities import Base

class Potential(Base):
    def __init__(self, adata):

        self.__parse__(locals())

    def _to_torch(self, X):
        if isinstance(X, np.ndarray):
            return torch.from_numpy(X).to(AutoDevice())
        elif isinstance(X, pd.Series):
            return torch.from_numpy(X.values).to(AutoDevice())
        else:
            raise ValueError("Non-recognizable input passed")

    def _configure_Laplacian(self):
        if not hasattr(self, "_L"):
            self._L = self.adata.obsp["Laplacian"]

    def _configure_R(self):
        if not hasattr(self, "_R"):
            self._R = self.adata.obs["R"]

    @property
    def R(self):
        self._configure_R()
        return self._R

    @property
    def L(self):
        self._configure_Laplacian()
        return self._L

    def _compute_L_inverse(self):
        if not hasattr(self, "_L_inv"):
            self._L_inv = torch.pinverse(self._to_torch(self.L).to(torch.float32))

    @property
    def L_inverse(self):
        self._compute_L_inverse()
        return self._L_inv

    def _compute_potential(self):
        if not hasattr(self, "_V"):
            self._V = torch.matmul(self.L_inverse.to(torch.float32), self._to_torch(self.R).to(torch.float32))

    @property
    def V(self):
        self._compute_potential()
        return self._V
    
def compute_potential(adata, key_added="V"):
    
    potential = Potential(adata, )
    adata.obs["V"] = potential.V.detach().cpu().numpy()
