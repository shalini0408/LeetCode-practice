class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            chars = list(word)
            print(chars)
            for i in range(len(chars)):
                original = chars[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue
                    chars[i] = c
                    newWord = ''.join(chars)
                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        # mark visited by removing it
                        wordSet.remove(newWord)
                # restore original character
                chars[i] = original
        return 0
            


