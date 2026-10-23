import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicts={}
        res = []
        for num in nums:
            if num not in dicts:
                dicts[num]=1
            else:
                dicts[num]+=1
        for key,value in dicts.items():
            if value > math.floor(len(nums)/3):
                res.append(key)
        return res
        