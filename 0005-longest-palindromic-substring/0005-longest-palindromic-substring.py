# class Solution(object):
#     def longestPalindrome(self, s):
#         maxi = 0
#         longest = ""

#         for i in range(0, len(s)):
#             for j in range(i+1, len(s)+1):
#                 if (s[i:j][::-1] == s[i:j]):
#                     if len(s[i:j][::-1]) > maxi:
#                         maxi = len(s[i:j][::-1])
#                         longest = s[i:j]
#         return longest
class Solution:
    def longestPalindrome(self, s):
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left = left + 1
                right = right - 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""