class Solution:
    def rob(self, nums: list[int]) -> int:
        memo={}
        def robs(index, nums,memo):
            if index in memo:
                return memo[index]
            if index>=len(nums):
                return 0
            res = max(nums[index]+robs(index+2,nums,memo), robs(index+1,nums,memo))
            memo[index]=res
            return res
        return robs(0,nums,memo)
        