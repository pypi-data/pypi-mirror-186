import pytest
import torch

from tests.utils.mock_data import create_struct_data, get_likelihoods
from torchlikelihoods import HeterogeneousObjectScaler
from torchlikelihoods import scalers_dict


def evaluate_transform(scaler, data):
    data_norm = scaler.transform(data, inplace=False)
    for key, value in data.__dict__.items():
        value_norm = getattr(data_norm, key)
        assert list(value_norm.shape) == list(value.shape)
    return data_norm


def evaluate_reconstruction(data, data_2):
    for key, value_2 in data_2.__dict__.items():
        value = getattr(data, key)

        assert list(value.shape) == list(value_2.shape)
        value_2 = value_2.type(value.dtype)
        cond = torch.isclose(value, value_2, atol=1e-3)
        assert cond.float().mean() == 1.0


def evaluate_inverse_transform(scaler, data, data_norm):
    data_2 = scaler.inverse_transform(data_norm, inplace=False)

    evaluate_reconstruction(data, data_2)


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
    num_samples = 16
    data = create_struct_data(num_samples,
                              lik_info)

    likelihoods = get_likelihoods(lik_info)
    sca_dict = {}
    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)


@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_standard_fit_manual(lik_info):
    num_samples = 16
    data = create_struct_data(num_samples,
                              lik_info)

    likelihoods = get_likelihoods(lik_info)
    sca_dict = {}
    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)

    scaler.fit_manual()


@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_standard_fit_het_data(lik_info):
    num_samples = 16
    data = create_struct_data(num_samples,
                              lik_info)

    likelihoods = get_likelihoods(lik_info)
    sca_dict = {}
    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)

    scaler.fit(data[0])

    data_norm = evaluate_transform(scaler, data[0])

    evaluate_inverse_transform(scaler, data[0], data_norm)

    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)

    scaler.fit(data)
    data_norm = scaler.transform(data, inplace=False)
    data_2 = scaler.inverse_transform(data_norm, inplace=False)
    for data_i, data_2_i in zip(data, data_2):
        evaluate_reconstruction(data_i, data_2_i)

    for data_i in data:
        data_norm = evaluate_transform(scaler, data_i)

        evaluate_inverse_transform(scaler, data_i, data_norm)


@pytest.mark.parametrize("lik_info", lik_info_choices)
def test_scalers_fit_het_data(lik_info):
    num_samples = 16
    data = create_struct_data(num_samples,
                              lik_info)

    likelihoods = get_likelihoods(lik_info)
    sca_dict = {}
    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    sca_dict['t'] = scalers_dict['scale_diff']()
    sca_dict['T'] = 't'
    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)

    scaler.fit(data[0])

    data_norm = evaluate_transform(scaler, data[0])

    evaluate_inverse_transform(scaler, data[0], data_norm)

    for i, lik in enumerate(likelihoods):
        name = f"{lik_info[i][0]}_{i}"
        sca_dict[name] = lik._get_scaler()

    scaler = HeterogeneousObjectScaler(scalers_dict=sca_dict)

    scaler.fit(data)
    data_norm = scaler.transform(data, inplace=False)
    data_2 = scaler.inverse_transform(data_norm, inplace=False)
    for data_i, data_2_i in zip(data, data_2):
        evaluate_reconstruction(data_i, data_2_i)

    for data_i in data:
        data_norm = evaluate_transform(scaler, data_i)

        evaluate_inverse_transform(scaler, data_i, data_norm)
