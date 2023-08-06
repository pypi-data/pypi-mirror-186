import pytest
import torch

from torch.distributions import Categorical

data_generator = {
    'normal': lambda n, d: torch.randn((n, d)),
    'cat': lambda n, d: torch.randint(0, d, (n, 1)),
    'cb': lambda n, d: torch.rand((n, d)),
    'ber': lambda n, d: torch.randint(0, 2, (n, d)),
}


def create_data(num_samples, num_categories):
    x = torch.randint(0, num_categories, (num_samples, 1))

    logits = torch.randn((num_samples, num_categories))
    x_one_hot = torch.nn.functional.one_hot(x.flatten(), num_classes=num_categories)
    return x.flatten(), x_one_hot, logits


@pytest.mark.parametrize("num_categories", [
    3,
    10,
])
def test_Categorical_create(num_categories):
    num_samples = 124
    x, x_one_hot, logits = create_data(num_samples, num_categories)
    x_index = x_one_hot.argmax(1)
    assert x_index.ndim == x.ndim
    assert list(x_index.shape) == list(x.shape)
    assert torch.eq(x, x_index).all()
    assert list(logits.shape) == [num_samples, num_categories]
    distr = Categorical(logits=logits)

    assert distr.probs.ndim == 2
    assert list(distr.probs.shape) == [num_samples, num_categories]


@pytest.mark.parametrize("num_categories", [
    3,
    10,
])
def test_Categorical_log_prob(num_categories):
    num_samples = 100
    x, x_one_hot, logits = create_data(num_samples, num_categories)
    x_index = x_one_hot.argmax(1)
    distr = Categorical(logits=logits)

    log_prob_1 = distr.log_prob(x)
    log_prob_2 = distr.log_prob(x_index)

    assert log_prob_1.ndim == log_prob_2.ndim
    assert log_prob_1.ndim == 1
    assert log_prob_1.shape[0] == num_samples
    assert log_prob_1.numel() == log_prob_2.numel()
    assert torch.eq(log_prob_1, log_prob_2).all()
