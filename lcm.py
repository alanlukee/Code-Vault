def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b, c):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    gcd = find_gcd(lcm, c)
    lcm = (lcm * c) // gcd
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

lcm = find_lcm(num1, num2, num3)
print("LCM:", lcm)