import math
class Solution(object):
    def maxSubArray(self, nums):
        # max_sum = nums[0]  
        # n = len(nums)

        # for i in range(n):
        #     sums = 0
        #     for j in range(i, n):
        #         sums += nums[j]  
        #         max_sum = max(max_sum, sums) 

        # return max_sum
       
        sums = float('-inf')
        max_num = 0
 
        for i in range(0, len(nums)):
            max_num = max_num + nums[i]
            if (sums < max_num):
                sums = max_num
 
            if max_num < 0:
                max_num = 0

        return sums




