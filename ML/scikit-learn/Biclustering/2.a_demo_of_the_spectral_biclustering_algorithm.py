print(__doc__)

import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import make_checkerboard
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score


n_clusters = (4, 3)
data, rows, colums = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10,
    shuffle=False, random_state=0)

plt.matshow(data, cmap= plt.cm.Blues)
plt.title("Original datasets")

#Shuffle clusters
rng= np.random.RandomState(0)
row_idx= rng.permutation(data.shape[0])
col_idx= rng.permutation(data.shape[1])
data= data[row_idx][:, col_idx]

plt.matshow(data, cmap= plt.cm.Blues)
plt.title("Shuffle datasets")

models= SpectralBiclustering(n_clusters= n_clusters, method='log', random_state=0)
models.fit(data)
score= consensus_score(models.biclusters_,(rows[:, row_idx], colums[:, col_idx]))

print("consensus score: {: .1f}".format(score))

fit_data= data[np.argsort(models.row_labels_)]
fit_data= fit_data[:, np.argsort(models.column_labels_)]

plt.matshow(fit_data, cmap= plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")

plt.matshow(np.outer(np.sort(model.row_labels_) + 1,
                     np.sort(model.column_labels_) + 1),
            cmap=plt.cm.Blues)
plt.title("Checkerboard structure of rearranged data")
plt.show()