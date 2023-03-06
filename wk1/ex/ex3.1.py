def iter_file(source):
    with open(source) as f:
        lines = f.readlines()
        heading = lines[0]
        heading_items = heading.strip().split(',')
        for line in lines[1:]:
            line_items = line.strip().split(',')
            result = {}
            for index, item in enumerate(heading_items):
                result[item] = line_items[index]
            yield result

def main():
    sample_file = 'test.csv'
    for item in iter_file(sample_file):
        print(item)

if __name__ == '__main__':
    main()