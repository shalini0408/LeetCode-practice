class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def climb(current,memo):
            if current in memo:
                return memo[current]
            if current == n:
                return 1
            if current>n:
                return 0
            ways = climb(current+1,memo)+climb(current+2,memo)
            if ways not in memo:
                memo[current]=ways
            return ways

        return climb(0,memo)
        