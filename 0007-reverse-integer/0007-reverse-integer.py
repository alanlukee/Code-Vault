class Solution(object):
    def reverse(self, x):
        k = str(x)
        stack = []
        for i in k:
            stack.append(i)
        olp = ""
        if stack[0] == '-':
            olp = olp + stack[0]
            stack.pop(0)
        while stack:
            olp = olp + stack.pop()

        reversed_int = int(olp)
        if reversed_int < -(2**31) or reversed_int > (2**31 - 1):
            return 0  
        return reversed_int
