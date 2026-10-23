class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        record = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        answers = []
        for idx in range(len(digits)):
            digit = digits[idx]
            answer = record[int(digit)]
            if not answers:
                answers = answer
            else:
                answers = [i+j for i in answers for j in answer]
        return answers