class Solution:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            
            #odd condition
            left = i
            right = i
            while(left>=0 and right<len(s) and s[left]==s[right]):
                count = count+1
                left = left-1
                right = right +1
                
            #even condition
            left = i
            right = i+1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                count = count+1
                left = left-1
                right = right +1
        return count
            
            