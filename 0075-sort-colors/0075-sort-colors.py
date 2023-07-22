class Solution(object):
    def sortColors(self, nums):
        zero_count = 0                   
        one_count = 0   
        two_count = 0
        for i in nums:
            if i==0:zero_count = zero_count + 1
            if i==1:one_count = one_count + 1
            if i==2:two_count = two_count + 1

        #nums = [2,0,2,1,1,0]
        # zero_count = 2                   
        # one_count = 2   
        # two_count = 2

        for i in range(zero_count):  #0,1  
            nums[i] = 0 
        for i in range(zero_count,zero_count+one_count): #2 -> 4    => 2,3
            nums[i] = 1
        for i in range(zero_count+one_count,zero_count+one_count+two_count ):
            nums[i] = 2
        return nums 
        

