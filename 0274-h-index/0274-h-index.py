class Solution(object):
    def hIndex(self, citations):
        
        citations.sort(reverse=True)
        
        for i,j in enumerate(citations):
            print(i,j)
            if i>=j:
                return i
        return len(citations)
    


        