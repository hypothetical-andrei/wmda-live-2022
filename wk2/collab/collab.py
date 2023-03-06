import data_sample
import distances

def top_matches(prefs, me, n=3, similarity=distances.euclidean):
    scores = [(similarity(prefs, me, other), other) for other in prefs if other != me]
    scores.sort()
    scores.reverse()
    return scores[:n]

def get_recommendations(prefs, me, n=3, similarity=distances.euclidean):
    totals = {}
    similarity_sums = {}
    for other in prefs:
        if other == me:
            continue
        sim = similarity(prefs, me, other)
        if sim == 0:
            continue
        for item in prefs[other]:
            if item not in prefs[me]:
                totals.setdefault(item, 0)
                similarity_sums.setdefault(item, 0)
                totals[item] = totals[item] + prefs[other][item] * sim
                similarity_sums[item] = similarity_sums[item] + sim
    rankings = [(total / similarity_sums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[:n]

def main():
    data = data_sample.critics
    # print(top_matches(data, 'Lisa Rose'))
    top_recommendations = get_recommendations(data, 'Toby')
    print(top_recommendations)

if __name__ == '__main__':
    main()