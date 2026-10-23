class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        def rec(memo,i, target):
            if (i,target) in memo:
                return memo[(i,target)]
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            take = rec(memo,i + 1, target - nums[i])
            memo[(i,target)]=take
            skip = rec(memo,i + 1, target)
            memo[(i,target)]=skip
            return take or skip
        return rec(memo,0, target)