class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind = -1
        reversed_nums=[]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if (ind == -1):
            nums.reverse()
            return

        for i in range(len(nums)-1,ind,-1):
            if nums[i]>nums[ind]:
                temp = nums[i]
                nums[i]= nums[ind]
                nums[ind] = temp
                break
        
        nums[ind + 1:] = reversed(nums[ind + 1:])