class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positionToBechanged = 1
        iterating = 1
        seen = nums[0]
        while iterating < len(nums):
            if nums[iterating] != seen:
                seen = nums[iterating]
                temp = nums[positionToBechanged]
                nums[positionToBechanged] = nums[iterating]
                nums[iterating] = nums[positionToBechanged]
                positionToBechanged+=1
            iterating+=1
        return positionToBechanged
        




            

        
        