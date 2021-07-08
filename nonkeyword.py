def add(**kwargs):
    print(type(kwargs))
    tmp = 0
    for key in kwargs:
        tmp = tmp + kwargs[key]
    return tmp
temp = add(a = 1, b = 2, c = 3, d = 4)
print(temp)