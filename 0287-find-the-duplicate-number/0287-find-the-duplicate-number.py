class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                return index
            nums[index]= -nums[index]
        