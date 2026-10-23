class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = {}
        def rec(num,memo):
            if num in memo:
                return memo[num]
            if num == 0:
                return 1
            if num<0:
                return 0
            ways = 0
            for i in nums:
                ways+=rec(num-i,memo)
                memo[num]=ways
            return ways
        return rec(target, memo)

        