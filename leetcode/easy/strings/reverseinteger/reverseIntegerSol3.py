class Solution:
    def reverse(self, x: int) -> int:

        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while modu > 0:
            modu, remainder = divmod(x, 10)
            res = res * 10 + remainder
        res *= sign
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

