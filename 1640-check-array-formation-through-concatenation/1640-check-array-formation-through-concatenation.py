class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={}
        for p in pieces:
            d[p[0]]=p
        idx=0
        while idx<len(arr):
            if arr[idx] in d:
                piece=d[arr[idx]]
                for p in piece:
                    if p!=arr[idx]:
                        return False
                    else:
                        idx+=1
            else:
                return False
        return True
                
        