import torch

from torchlikelihoods import MinMaxScaler
from tests.utils.mock_data import create_image_data, create_data
import pytest


def evaluate_fit(scaler, x, dims, expected_shape):
    scaler.fit(x, dims=dims)
    assert list(scaler.min_data.shape) == expected_shape
    assert list(scaler.max_data.shape) == expected_shape

    if dims == None:
        min_, max_ = x.min(), x.max()
        assert torch.isclose(scaler.min_data, min_, atol=1e-3)
        assert torch.isclose(scaler.max_data, max_, atol=1e-3)
    else:
        min_ = x.min(dims[0],keepdim=True)[0]
        max_ = x.max(dims[0],keepdim=True)[0]
        for dim in dims[1:]:
            min_ = min_.min(dim,keepdim=True)[0]
            max_ = max_.max(dim,keepdim=True)[0]

        assert torch.isclose(scaler.min_data, min_, atol=1e-3).all()
        assert torch.isclose(scaler.max_data, max_, atol=1e-3).all()







def evaluate_transform(scaler, x, dims):
    x_norm = scaler.transform(x)

    assert list(x_norm.shape) == list(x.shape)
    if dims == None:
        min_, max_ = x_norm.min(), x_norm.max()
        assert torch.isclose(min_, torch.tensor([scaler.min_]), atol=1e-3), f"min_data: {min_}"
        assert torch.isclose(max_, torch.tensor([scaler.max_]), atol=1e-3), f"max_data: {max_}"
    else:
        min_ = x_norm.min(dims[0],keepdim=True)[0]
        max_ = x_norm.max(dims[0],keepdim=True)[0]
        for dim in dims[1:]:
            min_ = min_.min(dim,keepdim=True)[0]
            max_ = max_.max(dim,keepdim=True)[0]
        assert torch.isclose(min_,  scaler.min_*torch.ones_like(min_), atol=1e-3).all()
        assert torch.isclose(max_,  scaler.max_* torch.ones_like(max_), atol=1e-3).all()

    return x_norm


def evaluate_inverse_transform(scaler, x, x_norm):
    x_1 = scaler.inverse_transform(x_norm)
    assert list(x_1.shape) == list(x.shape)
    cond = torch.isclose(x_1, x, atol=1e-3)
    assert cond.float().mean() == 1.0


@pytest.mark.parametrize("feature_range", [(0,1), (-1,1)])
def test_scalers_standard_create(feature_range):
    scaler = MinMaxScaler(feature_range=feature_range)

@pytest.mark.parametrize("feature_range", [(0,1), (-1,1)])
def test_scalers_standard_fit_manual(feature_range):
    scaler = MinMaxScaler(feature_range=feature_range)
    scaler.fit_manual()
    assert scaler.min_data == feature_range[0]
    assert scaler.max_data == feature_range[1]


@pytest.mark.parametrize("feature_range", [(0,1), (-1,1)])
def test_scalers_standard_fit_image_data(feature_range):
    num_samples = 100
    width, height, channels = (28, 28, 3)
    x = create_image_data(num_samples, width, height, channels).float()
    scaler = MinMaxScaler(feature_range=(0,1))
    evaluate_fit(scaler, x,
                 dims=None,
                 expected_shape=[])
    x_norm = evaluate_transform(scaler, x,
                                dims=None)

    evaluate_inverse_transform(scaler, x, x_norm)
    scaler.reset()

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
@pytest.mark.parametrize("feature_range", [(0,1), (-1,1)])
def test_scalers_standard_fit_het_data_index(lik_info, feature_range):
    num_samples = 100

    x, x_one_hot = create_data(num_samples, lik_info)
    scaler = MinMaxScaler(feature_range=feature_range)
    evaluate_fit(scaler, x,
                 dims=(0,),
                 expected_shape=[1, x.shape[1]])

    x_norm = evaluate_transform(scaler, x,
                                dims=(0,))

    evaluate_inverse_transform(scaler, x, x_norm)

@pytest.mark.parametrize("lik_info", lik_info_choices)
@pytest.mark.parametrize("feature_range", [(0,1), (-1,1)])
def test_scalers_standard_fit_het_data_one_hot(lik_info, feature_range):
    num_samples = 100

    x, x_one_hot = create_data(num_samples, lik_info)
    scaler = MinMaxScaler(feature_range=feature_range)
    evaluate_fit(scaler, x_one_hot,
                 dims=(0,),
                 expected_shape=[1, x_one_hot.shape[1]])

    x_norm = evaluate_transform(scaler, x_one_hot,
                                dims=(0,))

    evaluate_inverse_transform(scaler, x_one_hot, x_norm)


from torchlikelihoods.scalers import scalers_dict

@pytest.mark.parametrize("name", ['minn1_max1', 'min0_max1' ])
def test_scalers_minmax_dict(name):
    num_samples = 100
    width, height, channels = (28, 28, 3)
    x = create_image_data(num_samples, width, height, channels).float()
    scaler = scalers_dict[name]()
    evaluate_fit(scaler, x,
                 dims=None,
                 expected_shape=[])
    x_norm = evaluate_transform(scaler, x,
                                dims=None)

    evaluate_inverse_transform(scaler, x, x_norm)
    scaler.reset()

    evaluate_fit(scaler, x,
                 dims=(0, 2, 3),
                 expected_shape=[1, 3, 1, 1])

    x_norm = evaluate_transform(scaler, x,
                                dims=(0, 2, 3))

    evaluate_inverse_transform(scaler, x, x_norm)
