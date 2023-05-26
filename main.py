import numpy as np
from sklearn.utils.extmath import randomized_svd
from sklearn.mixture import GaussianMixture

adj = np.genfromtxt(fname="Public Whip Data/adjacency.txt", dtype=int)
U, s, Vh = randomized_svd(adj, n_components=2, random_state=0)
print(U.shape, s.shape, Vh.shape)

# gm = GaussianMixture().fit(adj)

