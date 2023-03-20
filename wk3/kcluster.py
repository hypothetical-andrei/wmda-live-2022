import distances
import random
import loaders
from sklearn.datasets import load_iris

def kcluster(rows, distance=distances.euclidean, k=4):
    MAX_ITER = 100
    intervals = [(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]
    clusters = [[random.random() * (intervals[i][1] - intervals[i][0]) + intervals[i][0] for i in range(len(rows[0]))] for j in range(k)]
    last_matches = None
    for t in range(MAX_ITER):
        best_matches = [[] for i in range(k)]
        for j in range(len(rows)):
            current_row = rows[j]
            best_match = 0
            for i in range(k):
                d = distance(clusters[i], current_row)
                if d < distance(clusters[best_match], current_row):
                    best_match = i
            best_matches[best_match].append(j)
        if best_matches == last_matches:
            break
        for i in range(k):
            avgs = [0.0] * len(rows[0])
            if len(best_matches[i]) > 0:
                for row_id in best_matches[i]:
                    for j in range(len(rows[row_id])):
                        avgs[j] += rows[row_id][j]
                for j in range(len(avgs)):
                    avgs[j] /= len(best_matches[i])
                clusters[i] = avgs
        last_matches = best_matches
    return best_matches

def main():
    # colnames, rownames, data = loaders.load_blog_data()
    MAX_CLUSTERS = 3
    # clusters = kcluster(data, k = MAX_CLUSTERS)
    # print(clusters)
    data = load_iris()
    # print(data)
    clusters = kcluster(data.data, k = MAX_CLUSTERS)
    cluster_structure = []
    # print(clusters)
    for cluster in clusters:
        cluster_structure.append((len([x for x in cluster if data.target[x] == 0]), len([x for x in cluster if data.target[x] == 1]), len([x for x in cluster if data.target[x] == 2])))
    cluster_purities = [max(x)/sum(x) for x in cluster_structure]
    print(cluster_purities)

if __name__ == '__main__':
    main()