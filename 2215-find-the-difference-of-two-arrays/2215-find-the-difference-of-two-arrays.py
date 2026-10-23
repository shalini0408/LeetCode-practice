class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        res = []
        res1 = []
        res2 = []
        for i in nums1:
            if i not in nums2:
                res1.append(i)

        for j in nums2:
            if j not in nums1:
                res2.append(j)
        res.append(res1)
        res.append(res2)
        return res
        
                
            




        