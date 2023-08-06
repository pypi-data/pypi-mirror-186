
from .._utilities._base_class import Base

from umap import UMAP


class AnnDataUMAP(Base):
    def __init__(self, n_components=50, **kwargs):

        self.__parse__(locals())
        self.umap = UMAP(n_components=self.n_components, **kwargs)

    def __call__(self, adata, use_key="X_pca"):

        adata.obsm["X_umap"] = self.umap.fit_transform(adata.obsm[use_key])


def umap(adata, n_components=2, return_model=False, **kwargs):

    adata_umap = AnnDataUMAP(n_components=n_components, **kwargs)
    adata_umap(adata)
    
    if return_model:
        return adata_umap.umap