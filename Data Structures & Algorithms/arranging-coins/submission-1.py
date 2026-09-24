class Solution:
    def arrangeCoins(self, n: int) -> int:
        c = 0
        level = 0

        if n == 1:
            return 1

        while n > 0:
            level += 1
            n -= level
            if n > 0:
                c += 1
        return c