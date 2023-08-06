import itertools

import pytest
import torch

from tests.utils.mock_data import create_data, get_likelihoods
from torchlikelihoods import likelihood_dict
from torchlikelihoods.distributions import HeterogeneousDistribution




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
def test_HeterogeneousDistribution_log_prob(lik_info, norm_categorical, norm_by_dim):
    num_samples = 100
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)

    distr = HeterogeneousDistribution(likelihoods=likelihoods,
                                      norm_categorical=norm_categorical,
                                      norm_by_dim=norm_by_dim)

    logits = torch.randn((num_samples, distr.params_size))
    distr.set_logits(logits)

    log_prob = distr.log_prob(x)

    assert log_prob.ndim == 2
    assert log_prob.shape[1] == distr.domain_size(False)

    log_prob = distr.log_prob(x_one_hot)

    assert log_prob.ndim == 2
    assert log_prob.shape[1] == distr.domain_size(False)


@pytest.mark.parametrize("lik_info,norm_categorical,norm_by_dim", options)
def test_HeterogeneousDistribution_mean(lik_info, norm_categorical, norm_by_dim):
    num_samples = 100
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)

    distr = HeterogeneousDistribution(likelihoods=likelihoods,
                                      norm_categorical=norm_categorical,
                                      norm_by_dim=norm_by_dim)

    logits = torch.randn((num_samples, distr.params_size))
    distr.set_logits(logits)
    mean = distr.mean

    assert mean.ndim == 2
    assert mean.shape[0] == num_samples
    assert mean.shape[1] == distr.domain_size(True)


@pytest.mark.parametrize("lik_info,norm_categorical,norm_by_dim", options)
def test_HeterogeneousDistribution_sample(lik_info, norm_categorical, norm_by_dim):
    num_samples = 100
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)

    distr = HeterogeneousDistribution(likelihoods=likelihoods,
                                      norm_categorical=norm_categorical,
                                      norm_by_dim=norm_by_dim)

    logits = torch.randn((num_samples, distr.params_size))
    distr.set_logits(logits)
    sample = distr.sample(one_hot=True)
    assert list(sample.shape) == [num_samples, distr.domain_size(True)]
    sample_index = distr.sample(one_hot=False)
    assert list(sample_index.shape) == [num_samples, distr.domain_size(False)]

#
# assert mean.ndim == 2
# assert  mean.shape[0] == num_samples
# assert  mean.shape[1] == distr.domain_size_one_hot
