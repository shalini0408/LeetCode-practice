class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        for i in range(len(nums)):
            if(nums[i]<target):
                l=l+1
        return l
        