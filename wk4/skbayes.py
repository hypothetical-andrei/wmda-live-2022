from sklearn.naive_bayes import GaussianNB
import loaders

def main():
    data = loaders.get_spam_features_sk('spambase')
    samples = data[400:]
    tests = data[:400]
    
    sample_features = [item['features'] for item in samples]
    sample_outcomes = [item['outcome'] for item in samples]
    test_features = [item['features'] for item in tests]
    test_outcomes = [item['outcome'] for item in tests]

    gnb = GaussianNB()
    classifier = gnb.fit(sample_features, sample_outcomes)
    predicted = classifier.predict(test_features)

    correct = len([item for item in zip(test_outcomes, predicted) if item[0] == item[1]])
    print(f'correct: {correct}/400')

if __name__ == '__main__':
    main()