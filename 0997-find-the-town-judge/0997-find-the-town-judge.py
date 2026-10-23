class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)
        for arr in trust:
            outdegree[arr[0]]+=1
            indegree[arr[1]]+=1
        for j in range(1,n+1):
            if outdegree[j]==0 and indegree[j] == n-1:
                return j
        return -1
            