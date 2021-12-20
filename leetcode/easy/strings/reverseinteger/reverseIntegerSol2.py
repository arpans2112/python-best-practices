class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x > 0 else (int(str(abs(x))[::-1]) * -1)
        return 0 if (result > 2147483647 or result < -2147483647) else result