my_list = ['a', 'b', 'c', 'd']
print(my_list)
my_list.append('e')
print(my_list)
my_list.extend(['f', 'g'])
print(my_list)
print(my_list[2])
print(my_list[1:3])
print(my_list[1:])
print(my_list[:4])
print(my_list[:])
print(my_list[:-1])

for item in my_list:
    print(item, end=' - ')

print()

my_tuple = (1, 'a', 10, 'b')
print(my_tuple)

for index, item in enumerate(my_list):
    # print(f'my_list[{index}]={item}')
    print('my_list[{index}]={item}'.format(index = index, item = item))

numbers = []
for i in range(0, 10):
    numbers.append(i)

print(numbers)