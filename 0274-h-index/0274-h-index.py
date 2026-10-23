class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
        
        
            