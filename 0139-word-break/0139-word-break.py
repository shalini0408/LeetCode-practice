class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}
        def rec(memo,i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for end in range(i+1,len(s)+1):
                temp = s[i:end]
                if temp in wordDict:
                    if rec(memo,end):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        
        return rec(memo,0)