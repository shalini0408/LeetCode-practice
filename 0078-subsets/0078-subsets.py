class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        subsets=[]
        for i in range(1<<length):
            subset = []
            for j in range(length):
                if i & (1<<j):
                    subset.append(nums[j])
                    print(subset)
            subsets.append(subset)
        return subsets
        