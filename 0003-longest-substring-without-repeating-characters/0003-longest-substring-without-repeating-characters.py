class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        charSet=set()
        l=0
        length = 0
        for r in range(0,len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l=l+1
            charSet.add(s[r])
            length = max(length, (r-l) +1)
        return length

        