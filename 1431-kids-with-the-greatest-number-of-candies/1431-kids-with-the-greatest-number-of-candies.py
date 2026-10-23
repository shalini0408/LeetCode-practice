class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= max_num:
                candies[i] = True
            else:
                candies[i] = False
        return candies