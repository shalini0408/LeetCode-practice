class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1, set2 = set(word1), set(word2)
        sortOccList1 = sorted([word1.count(x) for x in set1])
        sortOccList2 = sorted([word2.count(x) for x in set2])
        print(sortOccList1)
        print(sortOccList2)
        return (sortOccList1 == sortOccList2) and (set1 == set2) 