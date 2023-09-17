def check(n):

    if n==0 or n==1:
        return False
    flag = True
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            flag = False
            return flag
        else:
            flag = True

    if flag ==True:
        return flag
    
print("check prime:")
n = int(input())
k = check(n)


