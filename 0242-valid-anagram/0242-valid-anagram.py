class Solution(object):
    def isAnagram(self, s, t):
        dict_1 = {}
        dict_2 = {}
        for i in s:
            if i not in dict_1:
                dict_1[i] = 1
            else:
                dict_1[i] = dict_1[i] +1
        for i in t:
            if i not in dict_2:
                dict_2[i] = 1
            else:
                dict_2[i] = dict_2[i] +1
        if dict_1.items() == dict_2.items():
            return True
        else:
            return False
