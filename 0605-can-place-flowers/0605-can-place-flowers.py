class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        fb = len(flowerbed)
        if fb == 1:
            if flowerbed[0]==1:
                return False
            if flowerbed[0]==0 and n==1:
                return True
            if flowerbed[0]==0 and n>1:
                return False
            
        for i in range(fb):
            if flowerbed[i] == 0:
                if i==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -=1
                elif i==fb-1 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    n-=1
                elif flowerbed[i-1] == 0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1 
                if n == 0:
                    return True

        return False

                    
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         if n == 0:
#             return True

#         fb = len(flowerbed)
#         flag = False

#         if fb == 1:
#             if flowerbed[0] == 1:
#                 return False
#             if flowerbed[0] == 0 and n == 1:
#                 return True

#         for i in range(fb):
#             if flowerbed[i] == 0:
#                 if i == 0 or flowerbed[i - 1] == 0:
#                     if i == fb - 1 or flowerbed[i + 1] == 0:
#                         flowerbed[i] = 1
#                         n -= 1

#             if n == 0:
#                 return True

#         return False

        # noe = ""
        # fboe = ""
        # if n%2 == 0:
        #     noe = "even"
        # else:
        #     noe = "odd"
        # if (fb-2) %2 ==0:
        #     fboe = "even"
        # else:
        #     fboe = "odd"
        
        # if fboe =="even" and noe =="odd":
        #     return False
        # elif fboe =="odd" and noe =="even":
        #     return True
        # elif fboe =="even" and noe =="even":
        #     return False
        # elif fboe =="even" and noe =="even":
        #     return True
        # else:
        #     return True

