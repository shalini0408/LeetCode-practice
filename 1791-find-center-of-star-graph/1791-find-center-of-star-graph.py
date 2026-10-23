class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n= len(edges)+1
        degrees = [0]*(n+1)
        for arr in edges:
            degrees[arr[0]]+=1
            degrees[arr[1]]+=1
        for i in range(1,n+1):
            if degrees[i]==n-1:
                return i
        return -1