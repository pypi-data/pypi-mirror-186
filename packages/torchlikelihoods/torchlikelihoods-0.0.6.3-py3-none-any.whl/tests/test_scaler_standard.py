import torch

from torchlikelihoods import StandardScaler
from tests.utils.mock_data import create_image_data, create_data
import pytest


def evaluate_fit(scaler, x, dims, expected_shape):
    scaler.fit(x, dims=dims)
    assert list(scaler.mu_.shape) == expected_shape
    assert list(scaler.scale_.shape) == expected_shape


def evaluate_transform(scaler, x, dims):
    x_norm = scaler.transform(x)
    mu = x_norm.mean()
    assert torch.isclose(mu, torch.Tensor([0.0]), atol=1e-3)

    if dims == None:
        assert torch.isclose(mu, torch.Tensor([0.0]), atol=1e-3)
    else:
        std = x_norm.std(dims)

        for std_i in std:
            assert torch.isclose(std_i, torch.Tensor([1.0]), atol=1e-3)
    return x_norm


def evaluate_inverse_transform(scaler, x, x_norm):
    x_1 = scaler.inverse_transform(x_norm)
    assert list(x_1.shape) == list(x.shape)
    cond = torch.isclose(x_1, x,rtol=1e-04, atol=1e-04)
    assert cond.float().mean() == 1.0


def test_scalers_standard_create():
    scaler = StandardScaler()


def test_scalers_standard_fit_manual():
    scaler = StandardScaler()
    scaler.fit_manual()
    assert scaler.mu_ == 0.0
    assert scaler.scale_ == 1.0


def test_scalers_standard_fit_image_data():
    num_samples = 100
    width, height, channels = (28, 28, 3)
    x = create_image_data(num_samples, width, height, channels).float()
    scaler = StandardScaler()
    evaluate_fit(scaler, x,
                 dims=None,
                 expected_shape=[])
    x_norm = evaluate_transform(scaler, x,
                                dims=None)

    evaluate_inverse_transform(scaler, x, x_norm)

    evaluate_fit(scaler, x,
                 dims=(0, 2, 3),
                 expected_shape=[1, 3, 1, 1])

    x_norm = evaluate_transform(scaler, x,
                                dims=(0, 2, 3))

    evaluate_inverse_transform(scaler, x, x_norm)


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
def test_scalers_standard_fit_het_data(lik_info):
    num_samples = 100

    x, x_one_hot = create_data(num_samples, lik_info)
    scaler = StandardScaler()
    evaluate_fit(scaler, x,
                 dims=None,
                 expected_shape=[])
    x_norm = evaluate_transform(scaler, x,
                                dims=None)

    evaluate_inverse_transform(scaler, x, x_norm)
