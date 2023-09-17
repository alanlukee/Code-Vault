print("Find factors:")
n = int(input())
i = 2
factors = []
while(i*i<=n):
    if n % i :
        i = i+1
    else:
        n = n // i
        factors.append(i)
if n>1:
    factors.append(n)
print(factors)