class Solution(object):
    def removeElement(self, nums, val):
        new_index = 0
        current_index = 0
        while new_index < len(nums) and current_index < len(nums):
            if nums[current_index] == val:
                current_index += 1
            else:
                nums[new_index] = nums[current_index]
                new_index += 1
                current_index += 1
        return new_index
                
                
        
                
        
        