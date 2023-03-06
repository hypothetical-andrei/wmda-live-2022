def my_function(a, b, c, d = 10, e = 11):
    return a + b + c + d + e

print(my_function(1, 2, 3))
print(my_function(1, 2, 3, 4, 5))
print(my_function(1, 2, 3, e = 5))

my_list = [1, 2, 3, 4, 5]

def my_transformation(x):
    return x * 2

print(list(map(my_transformation, my_list)))

print(list(map(lambda x: x * 3, my_list)))

print([x * 4 for x in my_list if x > 3])
