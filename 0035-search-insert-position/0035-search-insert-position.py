class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                i = mid +1
            else:
                j = mid -1
        
        return i 


        