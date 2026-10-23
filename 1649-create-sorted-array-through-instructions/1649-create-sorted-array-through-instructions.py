class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        s=SortedList()
        ans=0
        for i in instructions:
            ans+=min(s.bisect_left(i),len(s)-s.bisect_right(i))
            s.add(i)
        return ans%((10**9)+7)
        
                       
                
                
        