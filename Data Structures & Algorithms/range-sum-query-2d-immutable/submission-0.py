class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        rows,cols=len(matrix),len(matrix[0])
        self.prefixSum = [[0] * cols for _ in range(rows)]
        for i in range (rows):
            for j in range (cols):
                top=self.prefixSum[i-1][j] if i>0 else 0
                left=self.prefixSum[i][j-1] if j>0 else 0
                diag=self.prefixSum[i-1][j-1] if (i>0 and j>0) else 0
                self.prefixSum[i][j]=matrix[i][j]+top+left-diag
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.prefixSum[row2][col2]
        top=self.prefixSum[row1-1][col2] if row1>0 else 0
        left=self.prefixSum[row2][col1-1] if col1>0 else 0
        diag=self.prefixSum[row1-1][col1-1] if row1>0 and col1>0 else 0
        rangeSum=total-top-left+diag
        return rangeSum

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)