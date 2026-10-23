class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        memo={}
        def rec(i,memo):
            if i in memo:
                return memo[i]
            longest = 1
            if i>len(nums)-1:
                return 0
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    length=1+rec(j,memo)
                    longest = max(longest,length)
                    memo[i]=longest
            return longest
        longests = 0
        for i in range(0,len(nums)):
            longests = max(longests,rec(i,memo))
        return longests
            
