class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] =1
            else:
                dict[i] = dict[i] +1
        flag = True
        for i ,j in dict.items():
            if j>=2:
                return True
                break
            else:
                flag = False
                
        if flag == False:
            return False