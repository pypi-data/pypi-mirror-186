

import os

import torch

from tests.utils.mock_data import create_struct_data

from torchlikelihoods.utils.struct import Struct

lik_info = [
        ('normal', 1),
        ('normal', 1),
        ('normal', 5),
        ('cat', 10),  # Number of categories
        ('cb', 2),
        ('ber', 2),
   ]

data = create_struct_data(num_samples=16,
                          lik_info=lik_info)
# %%

from torchlikelihoods.scalers.heterogeneous_object import HeterogeneousObjectScaler
from torchlikelihoods.scalers import scalers_dict


scaler = scalers_dict['identity']()

# %%
scaler_dict = {
    'history': scalers_dict[''](),
    't': 'history',
    'mark': scalers_dict['minmax01']()
}
scaler = HeterogeneousObjectScaler(scalers_dict=scaler_dict)
print(scaler)
# %%
scaler = HeterogeneousObjectScaler(scalers_dict=scaler_dict)

# scaler.fit(x=data[0])
scaler.fit_with_list(x_list=data)

print(scaler)


# %%
seq_i = data[0]
print(seq_i)
seq_i_norm = scaler.transform(seq_i, inplace=False)
print(seq_i)
print(seq_i_norm)