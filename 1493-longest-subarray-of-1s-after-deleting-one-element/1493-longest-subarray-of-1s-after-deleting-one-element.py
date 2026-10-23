class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        
        left = 0
        max_count = 0
        zeros = 0 

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_count = max(max_count, right - left)

        return max_count

            

        
        