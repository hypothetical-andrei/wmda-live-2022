def get_spam_features(filename, threshold = 0.1):
    with open(filename + '.names') as f:
        names = [line.split(':')[0] for line in f.readlines()]
    results = []
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [float(item.strip()) for item in items]
            classification = items[-1]
            word_features = items[:-10]
            features = []
            for index, item in enumerate(word_features):
                if item > threshold:
                    features.append(names[index])
            result = {
                'features': features,
                'outcome': 'bad' if classification == 1 else 'good'
            }
            results.append(result)
    return results

def get_spam_features_sk(filename):
    results = []
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [float(item.strip()) for item in items]
            classification = items[-1]
            word_features = items[:-1]
            result = {
                'features': word_features,
                'outcome': 'bad' if classification == 1 else 'good'
            }
            results.append(result)
    return results

def get_car_data(filename):
    results = []
    with open(filename) as f:
        for line in f.readlines():
            items = line.split(',')
            items = [item.strip() for item in items]
            result = {
                'features': items[:-1],
                'outcome': items[-1]
            }
            results.append(result)
    return results

def main():
    # data = get_spam_features('spambase')
    # print(data[0:3])
    # data = get_spam_features_sk('spambase')
    # print(data[0:3])
    data = get_car_data('car.data')
    print(data[0:3])

if __name__ == '__main__':
    main()