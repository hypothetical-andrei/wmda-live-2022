from sample import sample
from math import log
import loaders
import random
from PIL import Image, ImageDraw

class DecisionNode:
    def __init__(self, col=-1, value=None, results=None, false_subtree = None, true_subtree = None):
        self.col = col
        self.value = value
        self.results = results
        self.false_subtree = false_subtree
        self.true_subtree = true_subtree

def unique_counts(rows):
    results = {}
    for row in rows:
        outcome = row[-1]
        results.setdefault(outcome, 0)
        results[outcome] += 1
    return results

def entropy(rows):
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(rows)
    h = 0.0
    for result, count in results.items():
        p = float(count / len(rows))
        h -= p * log2(p)
    return h

def divide_set(rows, column, value):
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        split_function = lambda row: row[column] >= value
    else:
        split_function = lambda row: row[column] == value
    true_set = [row for row in rows if split_function(row)]
    false_set = [row for row in rows if not split_function(row)]
    return (false_set, true_set)

def build_tree(rows, scoref=entropy):
    if len(rows) == 0:
        return DecisionNode()
    current_score = scoref(rows)
    best_gain = 0.0
    best_criterion = None
    best_sets = None
    column_count = len(rows[0]) - 1
    for column in range(0, column_count):
        column_values = {}
        for row in rows:
            column_values[row[column]] = 1
            for value in column_values.keys():
                (false_set, true_set) = divide_set(rows, column, value)
                p = float(len(false_set) / len(rows))
                gain = current_score - p * scoref(false_set) - (1 - p) * scoref(true_set)
                if gain > best_gain and len(false_set) > 0:
                    best_gain = gain
                    best_criterion = (column, value)
                    best_sets = (false_set, true_set) 
    if best_gain > 0.0:
        false_branch = build_tree(best_sets[0])
        true_branch = build_tree(best_sets[1])
        return DecisionNode(col=best_criterion[0], value=best_criterion[1], true_subtree = true_branch, false_subtree=false_branch)
    else:
        return DecisionNode(results=unique_counts(rows))

def print_tree(node, indent=''):
    if node.results != None:
        print(node.results)
    else:
        print(node.col, ':', node.value, '?')
        print(indent, 'True ->', end='')
        print_tree(node.true_subtree, indent=indent + ' ')
        print(indent, 'False ->', end='')
        print_tree(node.false_subtree, indent=indent + ' ')

def classify(item, node):
    if node.results != None:
        return node.results
    else:
        value = item[node.col]
        if isinstance(value, int) or isinstance(value, float):
            if value >= node.value:
                print(f'decision {node.col} >= {value}')
                branch = node.true_subtree
            else:
                print(f'decision {node.col} < {value}')
                branch = node.false_subtree
        else:
            if value == node.value:
                print(f'decision {node.col} == {value}')
                branch = node.true_subtree
            else:
                print(f'decision {node.col} != {value}')
                branch = node.false_subtree
        return classify(item, branch)

def get_width(node):
    if node.true_subtree == None and node.false_subtree == None:
        return 1
    else:
        return get_width(node.false_subtree) + get_width(node.true_subtree)

def get_height(node):
    if node.true_subtree == None and node.false_subtree == None:
        return 0
    else:
        return 1 + max(get_height(node.false_subtree), get_height(node.true_subtree))

def draw_tree(tree, file='tree.jpg'):
    w = get_width(tree) * 100
    h = get_height(tree) * 100 + 120
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_node(draw, tree, w / 2, 20)
    img.save(file, 'JPEG')

def draw_node(draw, node, x, y):
    if node.results != None:
        results = [f'{outcome}:{count}' for outcome, count in node.results.items()]
        text = ','.join(results)
        draw.text((x - 20, y), text, (0, 0, 0))
    else:
        false_width = get_width(node.false_subtree) * 100
        true_width = get_width(node.true_subtree) * 100
        left = x - (true_width + false_width) / 2
        right = x + (true_width + false_width) / 2
        print( f'{node.col}:{node.value}')
        draw.text((x - 20, y - 10), f'{node.col}:{node.value}', (0, 0, 0))
        draw.line((x, y, left + false_width / 2, y + 100), fill=(255, 0, 0))
        draw.line((x, y, right - true_width / 2, y + 100), fill = (0, 255, 0))
        draw_node(draw, node.false_subtree, left + false_width / 2, y + 100)
        draw_node(draw, node.true_subtree, right - true_width / 2, y + 100)

def main():
    # data = sample
    data = loaders.get_car_data('car.data')
    random.shuffle(data)
    test_data = data[:150]
    train_data = data[150:]
    tree = build_tree(data)
    # print_tree(tree)
    draw_tree(tree)
    # tree = build_tree(train_data)
    # test_sample = ['digg', 'USA', 'yes', 19]
    # result = classify(test_sample, tree)
    # print(result)
    # certain_count = 0
    # certainty_threshold = 0.9
    # for item in test_data:
    #     result = classify(item, tree)
    #     if max(result.values())/sum(result.values()) > certainty_threshold:
    #         certain_count += 1
    # print(certain_count / 150)

if __name__ == '__main__':
    main()