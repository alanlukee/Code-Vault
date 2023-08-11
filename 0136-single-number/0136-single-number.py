class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for i in nums:
            if i  in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        for i,j in dict.items():
            if j==1:
                return i
                