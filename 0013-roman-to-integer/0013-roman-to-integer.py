class Solution(object):
    def romanToInt(self, s):
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        count = 0
        for i in range(0,len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                count = count-dict[s[i]]
            else:
                count = count + dict[s[i]]
        return count+dict[s[-1]]


       

        

