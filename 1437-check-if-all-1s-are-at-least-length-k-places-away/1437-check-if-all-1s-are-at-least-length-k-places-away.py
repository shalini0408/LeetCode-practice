class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l=[]
        for i in range(len(nums)):
            if nums[i]==1:
                l.append(i)
        print(l)
        for j in range(len(l)-1):
            if (l[j+1]-l[j])-1>=k:
                continue
            else:
                return False
                break
        return True