# Graph Partition and Measures

Python3 code implementing 11 graph-aware measures (gam) for comparing graph partitions as well as a stable ensemble-based graph partition algorithm (ecg). This verion works with the igraph package. A version for networkx is also available: partition-networkx.

## Graph aware measures (gam)

The measures are respectively:
* 'rand': the RAND index
* 'jaccard': the Jaccard index
* 'mn': pairwise similarity normalized with the mean function
* 'gmn': pairwise similarity normalized with the geometric mean function
* 'min': pairwise similarity normalized with the minimum function
* 'max': pairwise similarity normalized with the maximum function

Each measure can be adjusted (recommended) or not, except for 'jaccard'.
Details can be found in: 

Valérie Poulin and François Théberge, "Comparing Graph Clusterings: Set partition measures vs. Graph-aware measures", https://arxiv.org/abs/1806.11494.

## Ensemble clustering for graphs (ecg)

This is a good, stable graph partitioning algorithm. Details for ecg can be found in: 

Valérie Poulin and François Théberge, "Ensemble clustering for graphs: comparisons and applications", Appl Netw Sci 4, 51 (2019). 
    https://doi.org/10.1007/s41109-019-0162-z

# Example

We need to import the supplied Python file partition_igraph.

```pyhon
import numpy as np
import igraph as ig
import partition_igraph
```

Next, let's build a graph with communities.

```python
P = np.full((10,10),.025)
np.fill_diagonal(P,.1)
## 1000 nodes, 10 communities
g = ig.Graph.Preference(n=1000, type_dist=list(np.repeat(.1,10)),
                        pref_matrix=P.tolist(),attribute='class')
## the 'ground-truth' communities
tc = {k:v for k,v in enumerate(g.vs['class'])}
```

Run Louvain and ecg:

```python
ml = g.community_multilevel()
ec = g.community_ecg(ens_size=32)
```

Finally, we show a few examples of measures we can compute with gam:

```python
## for 'gam' partition are either 'igraph.clustering.VertexClustering' or 'dict'
print('Adjusted Graph-Aware Rand Index for Louvain:',g.gam(ml,tc))
print('Adjusted Graph-Aware Rand Index for ECG:',g.gam(ec,tc))
print('\nJaccard Graph-Aware for Louvain:',g.gam(ml,tc,method="jaccard",adjusted=False))
print('Jaccard Graph-Aware for ECG:',g.gam(ec,tc,method="jaccard",adjusted=False))
```
