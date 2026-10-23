class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countZero=0
        countOne=0
        countTwo=0
        for i in nums:
            if i==0:
                countZero+=1
            elif i==1:
                countOne+=1
            else:
                countTwo+=1

        for j in range(0,len(nums)):
            if countZero>0:
                nums[j]=0
                countZero-=1
            elif countOne>0:
                nums[j]=1
                countOne-=1
            else:
                nums[j]=2
                countTwo-=1
        return nums
        