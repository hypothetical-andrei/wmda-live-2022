from sklearn import cluster
import numpy as np
import loaders
import itertools

def print_cluster(clusters, current_id, initial_value, labels = None, n = 0):
  for i in range(n):
    print(' ', end = '')
  if current_id < initial_value:
    if labels == None:
      print(current_id)
    else:
      print(labels[current_id])
  else:
    print('-')
    current_cluster = [c for c in clusters if current_id == c['id']][0]
    print_cluster(clusters, current_cluster['left'], initial_value, labels = labels, n = n + 1)
    print_cluster(clusters, current_cluster['right'], initial_value, labels = labels, n = n + 1)


def main():
    col_names, row_names, data = loaders.load_blog_data()
    data = np.array(data)
    clusterer = cluster.AgglomerativeClustering(compute_full_tree=True, n_clusters=2, linkage='complete')
    model = clusterer.fit(data)
    it = itertools.count(data.shape[0])
    v = [{'id': next(it), 'left': x[0], 'right':x[1]} for x in model.children_]
    print_cluster(v, v[-1]['id'], data.shape[0], labels = row_names)

if __name__ == '__main__':
    main()