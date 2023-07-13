class Solution(object):
    def setZeroes(self, matrix):
        rowSize = len(matrix)
        colSize = len(matrix[0])
        rowArr = [0]*rowSize
        colArr = [0]*colSize
        for i in range(0,rowSize):
            for j in range(0,colSize):
                if matrix[i][j]==0:
                    rowArr[i]=1
                    colArr[j]=1
        for i in range(0,rowSize):
            for j in range(0,colSize):
                if(rowArr[i]==1 or colArr[j]==1):
                    matrix[i][j]=0


        

        
        