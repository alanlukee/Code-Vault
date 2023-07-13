class Solution(object):
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        
        suml = 0
        sumr = sum(nums)
        
        i = 0
        
        for x in nums:
            sumr = sumr - x
            if suml == sumr:
                return i
            suml = suml + x
            i = i + 1
        
        return -1
    
    
        # while i <= j:
        #     if suml < sumr:
        #         suml += nums[i]
        #         i += 1
        #     elif suml > sumr:
        #         sumr -= nums[j]
        #         j -= 1
        #     else:
        #         return i
            
        # return -1
