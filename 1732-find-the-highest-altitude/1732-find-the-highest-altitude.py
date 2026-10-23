class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        prev = 0
        for i in range(len(gain)):
            res=0
            res = gain[i] + prev
            prev = res
            max_alt = max(max_alt,res)
        return max_alt
        