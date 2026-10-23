class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ""
        i=0
        j=0
        str1 = len(word1)
        str2 = len(word2)
        while i<str1 and j<str2:
            s = s+word1[i]+word2[j]
            i+=1
            j+=1
        
        if i< str1:
            s = s + word1[i:]
        if j< str2:
            s = s + word2[j:]
        
        return s

        