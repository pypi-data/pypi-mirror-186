__version__ = "0.0.6"
import igraph as ig
from .partition_igraph import (
    community_ecg,
    gam,
)
ig.Graph.community_ecg = community_ecg
ig.Graph.gam = gam

