# TorchLikelihoods

A library for handling likelihoods in PyTorch for any type of data



## Installation

Run the following to install

```
pip install torchlikelihoods
```

## Usage

```python
from torchlikelihoods import NormalLikelihood
import torch

num_samples, num_feats = 100, 5
normal_data = torch.randn((num_samples, num_feats))

lik = NormalLikelihood(domain_size=num_feats)

scaler =  lik.get_scaler()

print(f"Domain size: {lik.domain_size()}")
print(f"Params size: {lik.params_size()}")
```


## Do you want to get involved in the development?

```bash
pip install -e .[dev]
```



### Testing
To run the tests:

```bash
make test
pytest
```