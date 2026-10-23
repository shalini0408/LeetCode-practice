class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 0

            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            res.append(char)
            if count > 1:
                for digit in str(count):
                    res.append(digit)

        chars[:] = res
        return len(chars)