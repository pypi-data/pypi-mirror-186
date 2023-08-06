

from ._base_class import Base


import os
import numpy as np
from anndata import AnnData


class PBAData(Base):
    def __init__(self, data_dir, files=["R", "S", "X"]):

        self.__parse__(locals())
        self._load_files()

    def _data_path(self, file):
        return os.path.join(self.data_dir, "{}.npy".format(file))

    def _load_numpy(self, file):
        return np.load(self._data_path(file))

    def _load_files(self):
        [setattr(self, file, self._load_numpy(file)) for file in self.files]

    def _configure_adata(self):
        if not hasattr(self, "_adata"):
            self._adata = AnnData(
                self.X, dtype=self.X.dtype, obsm={"S": self.S}, obs={"R": self.R}
            )

    @property
    def adata(self):
        self._configure_adata()
        return self._adata

    def __repr__(self):
        return "PBA AnnData:\n{}".format(self.adata)