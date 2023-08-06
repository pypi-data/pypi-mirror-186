# torch-pba
PyTorch Implementation of [PBA](https://github.com/AllonKleinLab/PBA). [AnnData](https://anndata.readthedocs.io/en/latest/)-centric.

## Installation

From PYPI:
```SHELL
pip install torch-pba
```

Alternatively, install the development version from GitHub:
```SHELL
git clone https://github.com/mvinyard/torch-pba.git; cd torch-pba; pip install -e .
```

## Example use:

```python
from torch_pba import PBA
from anndata import read_h5ad

pba = PBA(adata=read_h5ad("./path/to/adata.h5ad"))

pba.build_kNN()
pba.compute_Laplacian()
pba.compute_potential()
pba.compute_fate_bias()
pba.compute_mean_first_passage_time()
```

Time to calculate Mean First Passage Time for the [example hematopoiesis dataset](https://github.com/AllonKleinLab/PBA/blob/master/example_datasets.zip) is **cut from 4+ hours to <10 mins**. In this example, I used a NVIDIA T4 GPU rented from GCP.

See more: [notebook]()


## Original work:
* GitHub: [AllonKleinLab/PBA](https://github.com/AllonKleinLab/PBA)
* Paper: [Weinreb et al., PNAS. DOI: 10.1073/pnas.1714723115. (2018).](https://www.pnas.org/doi/10.1073/pnas.1714723115#executive-summary-abstract)

## Note:
I have not contributed any methodological novelty in this library. The original implementation contains the novel application of a Laplace transform to a kNN Graph to obtain a potential value, pseudotime, etc. Here, I have simply adapted the library to PyTorch/CUDA. No formal benchmarking has been performed.

## Contact / questions:
mvinyard@broadinstitute.org
