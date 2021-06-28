def add(*args):
    print(type(args))
    tmp = 0
    for number in args:
        tmp = tmp + number 
    return tmp
temp = add(1, 3, 3, 5, 6, 7, 3)
print(temp)