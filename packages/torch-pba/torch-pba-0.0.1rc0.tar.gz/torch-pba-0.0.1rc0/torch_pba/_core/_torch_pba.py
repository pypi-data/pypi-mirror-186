
import anndata
from autodevice import AutoDevice

from .._utilities import Base


from ._compute_distance_matrix import compute_distance_matrix
from ._construct_kNN_graph import construct_kNN_graph
from ._compute_adjacency_matrix import compute_adjacency_matrix
from ._compute_Laplacian import compute_Laplacian
from ._compute_potential import compute_potential
from ._compute_fate_bias import compute_fate_bias
from ._compute_mean_first_passage_time import compute_mean_first_passage_time


class PBA(Base):
    def __init__(self, adata: anndata.AnnData):

        self.__parse__(locals())

    def build_kNN(self, use_key: str = "X_pca", k: int = 10, key_added: str = "edges"):

        compute_distance_matrix(self.adata, use_key=use_key)
        construct_kNN_graph(self.adata, k=k, key_added=key_added)

    def compute_Laplacian(
        self,
        edges_key: str = "edges",
        adjacency_key: str = "adjacency",
        key_added: str = "Laplacian",
    ):

        compute_adjacency_matrix(self.adata, edges_key=edges_key)
        compute_Laplacian(self.adata, key_added=key_added)

    def compute_potential(self, key_added: str = "V"):
        
        compute_potential(self.adata, key_added=key_added)
        
    def compute_fate_bias(self, D=1.0, adjacency_key="adjacency", potential_key="V", S_key="S"):
        
        compute_fate_bias(self.adata, D=D, adjacency_key=adjacency_key, potential_key=potential_key, S_key=S_key)

    def compute_mean_first_passage_time(self, D=1.0, R_key="R", adjacency_key="adjacency", device=AutoDevice()):
        
        compute_mean_first_passage_time(self.adata, D=D, R_key=R_key, adjacency_key=adjacency_key, device=device)
