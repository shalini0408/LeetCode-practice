class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        A = list(range(0,n+1))
        for i in A:
            if i == 0 or i == 1:
                continue
            elif i%2 == 0:
                A[i] = A[i//2]
            else:
                A[i] = A[i//2] + A[(i//2) + 1]
        return max(A)
        