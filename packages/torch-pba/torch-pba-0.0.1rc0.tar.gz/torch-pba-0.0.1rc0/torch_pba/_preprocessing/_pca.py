
from .._utilities._base_class import Base

from sklearn.decomposition import PCA


class AnnDataPCA(Base):
    def __init__(self, n_components=50):

        self.__parse__(locals())
        self.pca = PCA(n_components=self.n_components)

    def __call__(self, adata):

        adata.obsm["X_pca"] = self.pca.fit_transform(adata.X)
        adata.uns["pcs"] = self.pca.components_
        
def pca(adata, n_components=50):
    
    adata_pca = AnnDataPCA(n_components=n_components)
    return adata_pca(adata)