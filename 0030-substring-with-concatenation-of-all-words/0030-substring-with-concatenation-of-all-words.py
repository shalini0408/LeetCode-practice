class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size_word = len(words[0])
        word_count = len(words)
        size_L = size_word * word_count
        res = []
        if size_L > len(s):
            return res
        hash_map = dict()
        for i in range(word_count):
            if words[i] in hash_map:
                hash_map[words[i]] += 1
            else:
                hash_map[words[i]] = 1
  
        for i in range(0, len(s) - size_L + 1, 1):
            temp_hash_map = hash_map.copy()
            j = i
            count = word_count
            while j < i + size_L:
  
                word = s[j:j + size_word]
  
                if (word not in hash_map or 
                    temp_hash_map[word] == 0):
                    break
  
                else:
                    temp_hash_map[word] -= 1
                    count -= 1
                j += size_word
  
            if count == 0:
                res.append(i)
        return res
            
                
                
        