class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        zeroes = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zeroes]=nums[zeroes],nums[i]
                zeroes+=1
        return nums