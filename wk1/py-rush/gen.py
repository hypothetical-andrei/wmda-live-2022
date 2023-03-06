def my_generator(start, end, step):
    state = start
    while state <= end:
        yield state
        state = state + step

for item in my_generator(0, 10, 2):
    print(item)