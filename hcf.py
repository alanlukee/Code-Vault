def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def checkCoprime(a,b):
    k = gcd(a,b)
    if k==1:
        return True
    else:
        return False

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = gcd(num1, num2)
l = checkCoprime(num1,num2)
if l:
    print("CoPrimes")
else:
    print("Non coprimes")
print(f"The HCF of {num1} and {num2} is {hcf}")

