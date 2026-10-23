class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for i,ele in enumerate(nums):
            rightSum = rightSum - ele
            if leftSum == rightSum:
                return i
            leftSum+=ele
        return -1


        