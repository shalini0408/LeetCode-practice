def getStartIndex(nums,target,mid_index):
    start_index = mid_index
    while nums[start_index] == target:
        start_index -=1
        if start_index < 0:
            break
    return start_index +1 
    
def getendIndex(nums,target,mid_index):
    end_index = mid_index

    while nums[end_index] == target:
        end_index +=1
        if end_index > len(nums)-1:
            break
    return end_index -1
   
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left, right = 0, len(nums)
        while left < right :
            mid = left + (right - left)//2
            if nums[mid] >target:
                right = mid
            elif nums[mid] < target:
                left = mid +1
            else:
                return [getStartIndex(nums,target,mid),getendIndex(nums,target,mid)]
        return [-1,-1]