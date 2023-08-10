class Solution(object):
    def repeatedCharacter(self, s):
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
                if dict[i]==2:
                    return i
        return None


        

