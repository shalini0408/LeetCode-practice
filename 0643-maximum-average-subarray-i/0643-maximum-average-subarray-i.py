class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==1:
            return float(max(nums))
        low = 0
        high = k-1
        sums = sum(nums[:k])
        max_num = sums/k
        while high<len(nums)-1:
            sums-=nums[low]
            low+=1
            high+=1
            sums+=nums[high]
            if (sums/k)>max_num:
                max_num = (sums/k) 
        return max_num
        