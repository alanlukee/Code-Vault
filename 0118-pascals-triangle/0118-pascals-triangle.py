class Solution(object):
    def generate(self, numRows):

        pT = []
        for i in range(0,numRows):
            pasc = [1]*(i+1)

            if (i>=2):
                for j in range(1,i):
                    pasc[j] = pT[i-1][j] + pT[i-1][j-1]
            pT.append(pasc)
        return pT

        
        