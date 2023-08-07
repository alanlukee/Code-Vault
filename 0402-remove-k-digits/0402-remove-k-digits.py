class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for i in num:
            while(stack and stack[-1]>i and k>0):
                k = k-1
                stack.pop()
            stack.append(i)
        while(stack and k>0):
            stack.pop()
            k = k-1
        if not stack:
            return "0"
        return str(int("".join(stack)))


 # "1432219" 
