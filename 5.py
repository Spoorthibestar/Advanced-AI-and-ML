import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
labels_kmeans = kmeans.labels_
gmm = GaussianMixture(n_components=k, random_state=42).fit(X)
labels_gmm = gmm.predict(X)
score_kmeans = silhouette_score(X, labels_kmeans)
score_gmm = silhouette_score(X, labels_gmm)
print("K-Means Silhouette Score:", score_kmeans)
print("EM (GMM) Silhouette Score:", score_gmm)
if score_kmeans > score_gmm:
print("K-Means produced better clusters.")
else:
print(" EM (GMM) produced better clusters.")
plt.bar(["K-Means", "EM (GMM)"], [score_kmeans, score_gmm],
color=["skyblue", "lightgreen"])
plt.title("Clustering Silhouette Score Comparison (IRIS Dataset)")
plt.ylabel("Silhouette Score")
plt.ylim(0, 1)
plt.show()
