class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  
        arr = nums[-k:]  
        del nums[-k:]  

        nums[:0] = arr
        
        return nums