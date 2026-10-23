class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        def minCost(index,memo):
            if index in memo:
                return memo[index]
            if index>=len(cost):
                return 0
            res = cost[index] + min(minCost(index + 1,memo),minCost(index + 2,memo))
            memo[index]= res
            return res
        return min(minCost(0, memo),minCost(1, memo))
        