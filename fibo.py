def fibo(num):
    if num ==1:
        return 0
    elif num ==2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3,num+1):
            k = a + b
            a ,b = b, k
    print(b)

n = 7
fibo(n)