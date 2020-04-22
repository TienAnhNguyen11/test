from collections import defaultdict
import operator
from time import time

import numpy as np

from sklearn.cluster import SpectralCoclustering
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.cluster import v_measure_score

print(__doc__)

def number_normalizer(tokens):
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)

class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize= super().build_tokenizer()
        return lambda doc: list (number_normalizer(tokenize(doc)))

categories = ['alt.atheism', 'comp.graphics',
              'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
              'comp.windows.x', 'misc.forsale', 'rec.autos',
              'rec.motorcycles', 'rec.sport.baseball',
              'rec.sport.hockey', 'sci.crypt', 'sci.electronics',
              'sci.med', 'sci.space', 'soc.religion.christian',
              'talk.politics.guns', 'talk.politics.mideast',
              'talk.politics.misc', 'talk.religion.misc']
newsgroups = fetch_20newsgroups(categories= categories)
y_true= newsgroups.target

vectorizer = NumberNormalizingVectorizer(stop_words= 'english', min_df=5)
cocluster = SpectralCoclustering(n_clusters=len(categories),
                                 svd_method='arpack', random_state=0)
kmeans= MiniBatchKMeans(n_clusters=len(categories), batch_size=20000,
                        random_state=0)

print("Vectoeizing...")
X= vectorizer.fit_transform(newsgroups.data)

print("Coclustering...")
start_time = time()
cocluster.fit(X)
y_cocluster= cocluster.row_labels_
print("Done in {: .2}s. V-measure: {: .4f}".format(
    time()  - start_time,
    v_measure_score(y_cocluster, y_true)))

print("MimibatchKmeans...")
start_time= time()
y_kmeans= kmeans.fit_predict(X)
print("Done in {: .2f}. V-meansure: {: .4}".format(
    time() - start_time,
    v_measure_score(y_kmeans, y_true)))

feature_names= vectorizer.get_feature_names()
document_names= list(newsgroups.target_names[i]  for i in newsgroups.target)









