class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxi ,i= 0,0
        while i < len(nums):
            if nums[i] == 1:
                total+=1
            else:
                maxi=max(maxi,total)
                total = 0
            i+=1
        maxi=max(maxi,total)
        return maxi 

        