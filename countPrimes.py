def checkPrime(n):
    if n ==0 or n ==1:
        return False
    flag = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0 :
            flag = False
            return False
            
    if flag:
        return True
        
        
n = 100
arr = []
for i in range(2,n+1):
    if checkPrime(i):
        arr.append(i)
print(arr)
print(len(arr))