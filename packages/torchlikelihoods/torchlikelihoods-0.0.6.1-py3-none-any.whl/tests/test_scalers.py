from torchlikelihoods import StandardScaler

def test_scalers_standard_create():
    scaler = StandardScaler()

def test_scalers_standard_fit_manual():
    scaler = StandardScaler()
    scaler.fit_manual()
    assert scaler.mu_ == 0.0
    assert scaler.scale_ == 1.0