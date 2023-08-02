class Solution(object):
    def reverseWords(self, s):  
        x = s.split()
        w = ""
        for i in x[::-1]:
            w = w+i+" "
        return w[0:len(w)-1]