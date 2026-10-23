class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Clarifying Question
        #Assuming both of them are valid strings
        #Does our input has capital letters
        #Should the comparasion be case sensitive?
        # One approach
        # freq1 = dict()
        # freq2 = dict()
        # if(len(s) != len(t)):
        #     return False
        
        # for i in s:
        #     if i not in freq1:
        #         freq1[i] = 0
        #     else:
        #         freq1[i]+=1

        # for j in t:
        #     if j not in freq2:
        #         freq2[j] = 0
        #     else:
        #         freq2[j]+=1
        
        # return (freq1 == freq2)

        # Second Approach
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            freq[char] = freq.get(char, 0) - 1

        for value in freq.values():
            if value != 0:
                return False

        return True
        
        