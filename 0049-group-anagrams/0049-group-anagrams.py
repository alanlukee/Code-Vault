class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}
        for i in strs:
            b = sorted(i)
            sor = "".join(b)
            if sor not in dict:
                dict[sor] = [i]
            else:
                dict[sor].append(i)
        return dict.values()
        