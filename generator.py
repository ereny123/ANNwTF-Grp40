def square_list(n):
    for x in range(n):
        if x == 0:
            y = 1
            yield y
        else:
            y = x * 2
            yield y

for i in square_list(9):
    print("Meow " * i)