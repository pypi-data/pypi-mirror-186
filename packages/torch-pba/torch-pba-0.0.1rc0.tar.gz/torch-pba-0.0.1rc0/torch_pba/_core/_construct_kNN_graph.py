import numpy as np
import anndata

from .._utilities import Base


class kNN(Base):
    def __init__(self, adata, k=10, distances_key="X_dist"):

        edges = set([])
        self.__parse__(locals())
        self._configure_distances()
        self._configure_indices()

    def _configure_distances(self):
        if not hasattr(self, "_distances"):
            self._distances = self.adata.obsp[self.distances_key]

    def _configure_indices(self):
        if not hasattr(self, "_indices"):
            self._indices = np.argpartition(self.distances, self.k, axis=1)[:, : self.k]

    @property
    def distances(self):
        return self._distances

    @property
    def indices(self):
        return self._indices

    def _add_edge(self, i, j):
        if i != j:
            self.edges.add(tuple(sorted([i, j])))

    def __call__(self):
        for i in range(self.distances.shape[0]):
            for j in self.indices[i]:
                self._add_edge(i, j)

        return np.array(list(self.edges))


def construct_kNN_graph(
    adata: anndata.AnnData,
    k: int = 10,
    distances_key: str = "X_dist",
    key_added: str = "edges",
):

    Graph = kNN(adata, k=k, distances_key=distances_key)
    adata.uns[key_added] = Graph()