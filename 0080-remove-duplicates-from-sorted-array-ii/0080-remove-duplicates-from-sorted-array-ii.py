class Solution(object):
    def removeDuplicates(self, nums):
        dict = {}
        k = 0

        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

            if dict[i] <= 2:  
                nums[k] = i
                k += 1

        return k  

        
        




