class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        count = 1
        for i in range(len(nums)-1,-1,-1):
            if count == k:
                return nums[i]
            else:
                count = count+1
