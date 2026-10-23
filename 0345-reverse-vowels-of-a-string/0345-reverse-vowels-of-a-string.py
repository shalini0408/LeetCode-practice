class Solution:
    def reverseVowels(self, s: str) -> str:
        leftVowels = 0
        rightVowels = len(s)-1
        string = list(s)
        vowels =['A','E','I','O', 'U', 'a','e','i','o','u']
        while leftVowels<rightVowels:
            if string[leftVowels] in vowels and string[rightVowels] in vowels:
                string[leftVowels], string[rightVowels] = string[rightVowels],  string[leftVowels]
                leftVowels+=1
                rightVowels-=1
            elif string[leftVowels] in vowels and string[rightVowels] not in vowels:
                rightVowels-=1
            elif string[leftVowels] not in vowels and string[rightVowels] in vowels:
                leftVowels+=1
            else:
                rightVowels-=1
                leftVowels+=1
        return "".join(string)
        