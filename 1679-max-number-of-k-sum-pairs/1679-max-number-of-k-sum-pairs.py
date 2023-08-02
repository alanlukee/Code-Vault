class Solution(object):
    def maxOperations(self, nums, k):
        # arr= []
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if((nums[i]+nums[j]==k)and ((nums[j] and nums[i]) not in arr)):
        #             arr.append(nums[i])
        #             arr.append(nums[j])
        # return (len(arr)/2)
        nums.sort()
        # [1,3,3,3,4]
        i = 0
        j = len(nums) -1
        count = 0
        while(i<j):
            val = nums[i] + nums[j]

            if val ==k:
                i = i+1
                j = j -1
                count = count+1
                
            if val<k:
                i = i+1
            if val>k:
                j = j-1
        return count



