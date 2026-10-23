class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # while(k>0):
        #     i = len(nums) - 1
        #     while(i>0):
        #         temp = nums[i]
        #         nums[i]= nums[i-1]
        #         nums[i-1] = temp
        #         i-=1
        #     k-=1
        # return nums
        k = k%len(nums)
        left=0
        right= len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        l=0
        r = k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        l = k 
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        return nums
            

        