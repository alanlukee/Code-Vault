class Solution(object):
    def isSubsequence(self, s, t):
        len_s = len(s)
        len_t = len(t)
        i = 0 
        j = 0 
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len_s 