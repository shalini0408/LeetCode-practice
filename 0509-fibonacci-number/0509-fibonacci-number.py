class Solution:
    def fib(self, n: int) -> int:
        memo={}
        def calculate(n):
            if n in memo:
                return memo[n]
            if n<=0:
                return 0
            elif n==1:
                return 1
            else:
                memo[n]=calculate(n-1)+calculate(n-2)
            return memo[n]
        return calculate(n)
        