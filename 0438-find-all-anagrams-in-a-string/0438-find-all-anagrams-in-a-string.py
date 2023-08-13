class Solution(object):
    def findAnagrams(self, s, p):
        dict1 = {}
        for i in p:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] +1
        
        arr = []
        dict2 = {}
        for i in range(len(s)):
            if s[i] in dict2:
                dict2[s[i]] = dict2[s[i]] + 1
            else:
                dict2[s[i]] = 1
            if i>=len(p):
                if dict2[s[i-len(p)]] ==1:
                    del dict2[s[i-len(p)]]
                else:
                    dict2[s[i-len(p)]]    = dict2[s[i-len(p)]] -1
            if dict1 ==dict2:
                arr.append(i-len(p) +1)
        return arr
                  
        
        
        