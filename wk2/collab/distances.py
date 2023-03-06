import data_sample
from math import sqrt
import statistics
import loaders

def euclidean(prefs, me, other):
    shared = {}
    for item in prefs[me]:
        if item in prefs[other]:
            shared[item] = 1
    if len(shared) == 0:
        return 0
    square_sum = sum([pow(prefs[me][item] - prefs[other][item], 2) for item in prefs[me] if item in prefs[other]])
    return 1 / (1 + sqrt(square_sum))

def pearson(prefs, me, other):
    shared = {}
    for item in prefs[me]:
        if item in prefs[other]:
            shared[item] = 1
    if len(shared) == 0:
        return 0
    my_ratings = [prefs[me][item] for item in shared]
    other_ratings = [prefs[other][item] for item in shared]
    return statistics.correlation(my_ratings, other_ratings)

def main():
    # data = data_sample.critics
    data = loaders.load_movie_lens()
    # print(euclidean(data, 'Lisa Rose', 'Gene Seymour'))
    print(pearson(data, '5', '6'))

if __name__ == '__main__':
    main()