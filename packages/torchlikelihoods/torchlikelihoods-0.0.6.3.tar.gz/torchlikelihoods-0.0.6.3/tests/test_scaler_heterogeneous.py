import torch

from torchlikelihoods import HeterogeneousScaler
from tests.utils.mock_data import create_data, get_likelihoods
from tests.utils.mock_data import create_data
import pytest




def evaluate_transform(scaler, x, dims):
    x_norm = scaler.transform(x)
    assert list(x_norm.shape) == list(x.shape)
    return x_norm


def evaluate_inverse_transform(scaler, x, x_norm):
    x_1 = scaler.inverse_transform(x_norm)
    assert list(x_1.shape) == list(x.shape)
    cond = torch.isclose(x_1, x, atol=1e-3)
    assert cond.float().mean() == 1.0



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
@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_standard_create(lik_info):
    num_samples = 345
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)
    scalers= [lik._get_scaler() for lik in likelihoods]
    splits= [lik.domain_size() for lik in likelihoods]
    scaler = HeterogeneousScaler(scalers=scalers, splits=splits)

@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_standard_fit_manual(lik_info):
    num_samples = 345
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)
    scalers= [lik._get_scaler() for lik in likelihoods]
    splits= [lik.domain_size() for lik in likelihoods]
    scaler = HeterogeneousScaler(scalers=scalers, splits=splits)

    scaler.fit_manual()



@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_standard_fit_het_data(lik_info):
    num_samples = 345
    x, x_one_hot = create_data(num_samples,
                               lik_info)

    likelihoods = get_likelihoods(lik_info)
    scalers= [lik._get_scaler() for lik in likelihoods]
    splits= [lik.domain_size() for lik in likelihoods]
    scaler = HeterogeneousScaler(scalers=scalers, splits=splits)

    scaler.fit(x_one_hot, dims=(0,))


    x_norm = evaluate_transform(scaler, x_one_hot,
                                dims=(0,))

    evaluate_inverse_transform(scaler, x_one_hot, x_norm)
