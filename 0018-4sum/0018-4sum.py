class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,len(nums)-1
                while(l<r):
                    threesum=a+nums[j]+nums[l]+nums[r]
                    if threesum>target:
                        r=r-1
                    elif(threesum<target):
                        l=l+1
                    else:
                        res.append([a,nums[j],nums[l],nums[r]])
                        l=l+1
                        while nums[l]==nums[l-1] and l<r:
                            l=l+1
        return res
            
        