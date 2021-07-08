a = int(input('Please enter your lunch bill: '))

b = a
temp = a//1000
print(temp, '1000 Taka note(s)')
if temp > 0:
    a = a%1000
    b = a
else:
    a = b
temp = a//500
print(temp, "500 taka note(s).")
if temp >= 0:
    a = a%500
    b = a
else:
    a = b

temp = a//200
print(temp, "200 taka note(s).")
if temp >= 0:
    a = a%200
    b = a
else:
    a = b

temp = a//100
print(temp, "100 taka note(s).")
if temp >= 0:
    a = a%100
    b = a
else:
    a = b

temp = a//50
print(temp, "50 taka note(s).")
if temp >= 0:
    a = a%50
    b = a
else:
    a = b



temp = a//20
print(temp, "20 taka note(s).")
if temp >= 0:
    a = a%20
    b = a
else:
    a = b

temp = a//10
print(temp, "10 taka note(s).")
if temp >= 0:
    a = a%10
    b = a
else:
    a = b


temp = a//5
print(temp, "5 taka note(s).")
if temp >= 0:
    a = a%5
    b = a
else:
    a = b

temp = a//2
print(temp, "2 taka note(s).")
if temp >= 0:
    a = a%2
    b = a
else:
    a = b

temp = a//1
print(temp, "1 taka note(s).")
if temp >= 0:
    a = a%1
    b = a
else:
    a = b
