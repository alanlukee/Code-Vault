class Solution(object):
    def countPrimes(self, n):
        # if n <= 2:
        #     return 0
        # count = 0
        # for j in range(2, n):
        #     flag = True
        #     for i in range(2, int(j**0.5) + 1):  #from 2 to the square root of that number
        #         if j % i == 0:
        #             flag = False
        #             break
        #     if flag:
        #         count = count + 1

        # return count

        #SIEVE OF ERATOSTHENES

        # prime_arr = [True] * n
        # # print(prime_arr)
        # count = 0
        # num = 2
        # while(num*num <= n):
        #     if prime_arr[num]==True:
        #         for i in range(num*num, n, num):
        #             prime_arr[i]=False

        #     num = num+1
        # for j in prime_arr[2:]:
        #     if j==True:
        #         count = count+1
        # return count

        arr = [True] * n  
        if n == 0 or n == 1:
            return 0
        count = 0
        
        for i in range(2, int(n**0.5 + 1)):
            if arr[i] == True:
                for j in range(2*i, n, i):
                    arr[j] = False

        for i in arr[2:]:
            if i==True:
                count = count+1 
        return count
 