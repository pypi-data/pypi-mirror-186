import itertools

import pytest
import torch

from tests.utils.mock_data import create_data, get_likelihoods
from torchlikelihoods import HeterogeneousLikelihood

lik_info_choices = [
    [
        ('normal', 5),
    ],
    [
        ('normal', 5),
        ('cat', 10),  # Number of categories
        ('cb', 2),
        ('ber', 2),
    ],
    [
        ('normal', 5),
        ('cat', 10),  # Number of categories
        ('cb', 2),
        ('ber', 2),
        ('cat', 6),  # Number of categories
    ]
]
norm_cat_choices = [True, False]
norm_by_dim_choices = [True, False]
options = list(itertools.product(lik_info_choices, norm_cat_choices, norm_by_dim_choices))


@pytest.mark.parametrize("lik_info,norm_categorical,norm_by_dim", options)
def test_HeterogeneousLikelihood(lik_info, norm_categorical, norm_by_dim):
    num_samples = 100
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)

    lik = HeterogeneousLikelihood(likelihoods=likelihoods,
                                      norm_categorical=norm_categorical,
                                      norm_by_dim=norm_by_dim,
                                    one_hot_domain=True)

    logits = torch.randn((num_samples, lik.params_size()))

    distr = lik(logits, return_mean=False)

    scaler = lik.get_scaler(dataset=x_one_hot)