import loaders
import random

def get_features(item):
    return item['features']

class Classifier:
    def __init__(self, get_features):
        self.get_features = get_features
        self.cc = {}
        self.fc = {}
    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1
    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1
    def total_count(self):
        return sum(self.cc.values())
    def cat_count(self, cat):
        if cat in self.cc:
            return self.cc[cat]
        return 0
    def f_count(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return self.fc[f][cat]
        return 0
    def categories(self):
        return self.cc.keys()
    def train(self, item, cat):
        features = self.get_features(item)
        for f in features:
            self.incf(f, cat)
        self.incc(cat)
    def fprob(self, f, cat):
        if self.cat_count(cat) != 0:
            return self.f_count(f, cat) / self.cat_count(cat)
        return 0

class NaiveBayesClassifier(Classifier):
    def __init__(self, get_features):
        Classifier.__init__(self, get_features)
    def prob(self, item, cat):
        cat_prob = self.cat_count(cat) / self.total_count()
        message_probability = self.m_prob(item, cat)
        return cat_prob * message_probability
    def m_prob(self, item, cat):
        features = self.get_features(item)
        p = 1
        for f in features:
            p *= self.fprob(f, cat)
        return p
    def classify(self, item):
        max_prob = 0
        best_cat = None
        for cat in self.categories():
            prob = self.prob(item, cat)
            if prob > max_prob:
                max_prob = prob
                best_cat = cat
        return best_cat

def main():
    # data = loaders.get_spam_features('spambase')
    # random.shuffle(data)
    # samples = data[400:]
    # tests = data[:400]
    # classifier = NaiveBayesClassifier(get_features)
    # for item in samples:
    #     classifier.train(item, item['outcome'])
    # correct = 0
    # for item in tests:
    #     result = classifier.classify(item)
    #     if result == item['outcome']:
    #         correct += 1
    # print(f'correct: {correct}/400')
    data = loaders.get_car_data('car.data')
    # random.shuffle(data)
    samples = data[170:]
    tests = data[:170]
    classifier = NaiveBayesClassifier(get_features)
    for item in samples:
        classifier.train(item, item['outcome'])
    correct = 0
    for item in tests:
        result = classifier.classify(item)
        if result == item['outcome']:
            correct += 1
    print(f'correct: {correct}/170')

if __name__ == '__main__':
    main()