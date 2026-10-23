class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            first =nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                total= first + nums[left] + nums[right]
                if total == 0:
                    if [first,nums[left],nums[right]] not  in res:
                        res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return res
            

        