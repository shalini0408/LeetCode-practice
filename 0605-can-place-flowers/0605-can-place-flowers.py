class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                prev = 0 if i == 0 else flowerbed[i - 1]
                next_ = 0 if i == length - 1 else flowerbed[i + 1]

                if prev == 0 and next_ == 0:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True

        return n <= 0