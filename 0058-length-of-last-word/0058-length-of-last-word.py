class Solution(object):
    def lengthOfLastWord(self, s):
        if s==" ":
            return 0
        s=s.split()
        if(len(s)==0):
            return 0
        else:
            return len(s[-1])
        