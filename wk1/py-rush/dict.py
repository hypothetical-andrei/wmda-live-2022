my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(my_dict)

for k, v in my_dict.items():
    print(f'for {k} value is {v}')

if 'a' in my_dict:
    print('a exists in dict')