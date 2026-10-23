class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def dp(amt,memo):
            if amt in memo:
                return memo[amt]
            if amt==0:
                return 0
            if amt<0:
                return float('inf')
            minimum = float('inf')
            for coin in coins:
                result = 1+ dp(amt-coin,memo)
                minimum = min(minimum,result)
            memo[amt]=minimum
            return minimum

        memo={}
        result = dp(amount,memo)

        if result == float('inf'):
            return -1

        return result
            
        
        
        