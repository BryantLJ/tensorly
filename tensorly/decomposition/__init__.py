"""
The :mod:`tensorly.decomposition` module includes utilities for performing
tensor decomposition such as CANDECOMP-PARAFAC and Tucker.
"""

from .candecomp_parafac import parafac, non_negative_parafac
from ._tucker import tucker, non_negative_tucker
from .robust_decomposition import robust_pca
