class Solution(object):
    def isValid(self, s):
        openB = ['(', '{' , '[']
        closeB = [')', '}', ']']
        stack =[]
        dict={
            '(' : ')',
            '[' : ']',
            '{' : '}'

        }
        for i in s:
            if i in openB:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                else:

                    popB = stack.pop()
                    if i != dict[popB]:
                        return False
                    
        if len(stack)==0:
            return True

    