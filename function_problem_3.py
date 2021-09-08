def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

print("please input two integers: ")

a, b = map(int, input().split())

print("H.C.F of your given integers: ", gcd(a, b))
print("L.C.M of your given integers: ", lcm(a, b))