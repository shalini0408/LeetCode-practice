class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter=collections.Counter(nums)
        print(counter)
        ans=0
        for k in counter:
            if k+1 in counter and (counter[k]+counter[k+1])>ans:
                ans=counter[k]+counter[k+1]
        return ans