def get_car_data(filename):
    results = []
    with open(filename) as f:
        for line in f.readlines():
            items = line.split(',')
            items = [item.strip() for item in items]
            results.append(items)
    return results

def main():
    pass

if __name__ == '__main__':
    main()