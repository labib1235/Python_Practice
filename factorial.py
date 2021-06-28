def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number - 1)
        
print('please input the number:')
number = int(input())
print(factorial(number))