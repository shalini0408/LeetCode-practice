class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers =[0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
               stack_index = stack[-1]
               answers[stack_index] = i-stack_index
               stack.pop()
            stack.append(i)
        return answers
        
            

        