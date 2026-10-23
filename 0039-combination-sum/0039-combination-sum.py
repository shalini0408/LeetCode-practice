class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        self.findCombinationSum(0,candidates,target,result,[])
        return result
        #your code goes here
    def findCombinationSum(self, index, candidates, target, result, array):
        if index==len(candidates):
            if target==0:
                result.append(list(array))
        if index == len(candidates):
            return
        if candidates[index] <= target:
            array.append(candidates[index])
            self.findCombinationSum(index,candidates,target-candidates[index],result,array)
            array.pop()
        self.findCombinationSum(index+1,candidates, target, result,array)
        
        