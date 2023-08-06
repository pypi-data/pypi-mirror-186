"""This module contains type aliases and data types for type hints"""

__all__ = ["RealMatrix", "RealVector", "UncertainArray"]

from typing import NamedTuple, TypeAlias

import numpy as np
from numpy._typing import NDArray

RealMatrix: TypeAlias = NDArray[np.float64]
"""A real matrix represented by a :class:`np.ndarray <numpy.ndarray>`"""
RealVector: TypeAlias = NDArray[np.float64]
"""A real vector represented by a :class:`np.ndarray <numpy.ndarray>`"""


class UncertainArray(NamedTuple):
    """A tuple of a tensor of values with a tensor of associated uncertainties"""

    values: RealVector
    """the corresponding values"""
    uncertainties: RealMatrix | RealVector
    """... and their associated uncertainties"""
