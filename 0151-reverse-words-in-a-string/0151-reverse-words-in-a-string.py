class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        text = text[::-1]
        return " ".join(text)