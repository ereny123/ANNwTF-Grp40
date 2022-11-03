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
    
# Another way
def meow_gen():
    n = 1
    while n < 6:
        yield "Meow" * n
        n += 1
        
result = meow_gen()

for number, output in enumerate(result, start = 1):
    print(number, output)
