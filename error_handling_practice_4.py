try:
    a = 5
    b = 6
    print(a + b)

except ValueError as e:
    print(e)

else:
    print("There is no exception")