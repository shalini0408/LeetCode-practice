class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        res =[]
        for num in matrix:
            if target <= num[-1]:
                res.append(num)
                break
        
        if target in num:
            return True
        else:
            return False