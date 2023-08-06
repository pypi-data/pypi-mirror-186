
from .._utilities import Base
from tqdm.notebook import tqdm
from autodevice import AutoDevice

import torch
import numpy as np


class MeanFirstPassageTime(Base):
    def __init__(
        self, adata, D=1.0, R_key="R", adjacency_key="adjacency", device=AutoDevice()
    ):

        self.__configure__(locals())

    def __configure__(
        self, kwargs, ignore=["self"], private=["R_key", "adjacency_key"]
    ):

        self.__parse__(kwargs, ignore=ignore, private=private)

        self._n_cells = self.adata.shape[0]
        self._R = self.adata.obs[self._R_key]
        self._T = torch.zeros((self._n_cells, self._n_cells)).to(self.device).to(torch.float32)

    def row_sum_normalize(self, bigP):
        d = torch.sum(bigP, dim=1)
        return bigP / (torch.tile(d[:, None], (1, bigP.shape[1])))

    def _configure_A(self):
        if not hasattr(self, "_A"):
            self._A = self.adata.obsp[self._adjacency_key]

    @property
    def A(self):
        self._configure_A()
        return self._A

    def _configure_V(self):
        if not hasattr(self, "_V"):
            self._V = self.adata.obs["V"] / self.D

    @property
    def V(self):
        self._configure_V()
        return self._V

    def _configure_P(self):
        if not hasattr(self, "_P"):
            Vx, Vy = np.meshgrid(self.V, self.V)
            self._P = self.A * np.exp(np.minimum(Vy - Vx, 400))

    @property
    def P(self):
        self._configure_P()
        return self._P

    def _configure_identity_matrix(self):
        if not hasattr(self, "_identity_matrix"):
            self._identity_matrix = (
                torch.eye(self._n_cells - 1).to(torch.float32).to(self.device)
            )

    @property
    def identity_matrix(self):
        self._configure_identity_matrix()
        return self._identity_matrix

    def _configure_ones(self):
        if not hasattr(self, "_ones"):
            size = int(self._n_cells - 1)
            self._ones = torch.ones(size).to(self.device)

    @property
    def ones(self):
        self._configure_ones()
        return self._ones

    def _configure_bigP_init(self):
        if not hasattr(self, "_bigP_init"):
            bigP_init = np.zeros((self._n_cells + 1, self._n_cells + 1))
            bigP_init[: self._n_cells, : self._n_cells] = self.P
            bigP_init[: self._n_cells, -1] = -np.minimum(self._R, 0)
            bigP_init[-1, -1] = 1
            self._bigP_init = bigP_init

    @property
    def bigP_init(self):
        self._configure_bigP_init()
        return self._bigP_init

    def _configure_one(self):
        if not hasattr(self, "_one"):
            self._one = torch.Tensor([1.0]).to(self.device)

    @property
    def one(self):
        self._configure_one()
        return self._one.double()

    def _configure_cell_range(self):
        if not hasattr(self, "_cell_range"):
            self._cell_range = torch.arange(self._n_cells).to(self.device)

    @property
    def cell_range(self):
        self._configure_cell_range()
        return self._cell_range

    def forward(self, i):  # , I):

        bigP = torch.from_numpy(self.bigP_init).to(self.device)
        new_idx = torch.arange(self._n_cells + 1)
        new_idx = (
            torch.cat([new_idx[new_idx != new_idx[i]], torch.Tensor([i])])
            .to(self.device)
            .to(int)
        )
        bigP = bigP[new_idx, :][:, new_idx]
        bigP[-1, :] = 0
        bigP[-1, -1] = 1
        bigP = self.row_sum_normalize(bigP)
        Q = torch.Tensor(bigP[: self._n_cells - 1, : self._n_cells - 1]).to(self.device)
        RR = (
            torch.Tensor(bigP[: self._n_cells - 1, self._n_cells - 1 :])
            .to(torch.float32)
            .to(self.device)
        )
        N = torch.linalg.inv(self.identity_matrix - Q.to(torch.float32)).to(self.device)
        B = torch.matmul(N, RR).to(torch.float32).to(self.device)
        d = torch.diag(B[:, -1]).to(torch.float32).to(self.device)

        dinv = torch.diag(self.one / B[:, -1]).to(torch.float32).to(self.device)
        return torch.matmul(
            torch.matmul(torch.matmul(dinv, N), d),
            self.ones.to(torch.float32),
        ).nan_to_num()

    def __call__(self):

        T = self._T.to(torch.float32).to(self.device)

        for i in tqdm(range(self._n_cells)):
            T[self.cell_range != i, i] = self.forward(i)

        self.T = T.detach().cpu().numpy()
        return self.T
    
    
def compute_mean_first_passage_time(
    adata, D=1.0, R_key="R", adjacency_key="adjacency", device=AutoDevice()
):

    MFPT = MeanFirstPassageTime(
        adata, D=D, R_key=R_key, adjacency_key=adjacency_key, device=device
    )
    adata.obsp["MFPT"] = MFPT()