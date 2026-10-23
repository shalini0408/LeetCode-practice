class Solution(object):
    def generateRow(self,row):
        ans = 1
        ansRow = []
        ansRow.append(ans)
        for col in range(1,row):
            ans = ans * (row-col)
            ans = ans//col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans =[[1]]
        for i in range(2,numRows+1):
            ans.append(self.generateRow(i))
        return ans
        