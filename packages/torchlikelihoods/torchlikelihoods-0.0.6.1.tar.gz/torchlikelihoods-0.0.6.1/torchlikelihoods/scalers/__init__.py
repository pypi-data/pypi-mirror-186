from .minmax import MinMaxScaler
from .min import MinScaler
from .standard import StandardScaler
from .scale import ScaleScaler
from .scalediff import ScaleDiffScaler
from .identity import IdentityScaler
from .heterogeneous import HeterogeneousScaler
from .heterogeneous_object import HeterogeneousObjectScaler

scalers_dict = {
    'minmax01': MinMaxScaler,
    'min0': MinScaler,
    'std': StandardScaler,
    'scale': ScaleScaler,
    'scale_diff': ScaleDiffScaler,
    'identity': IdentityScaler
}