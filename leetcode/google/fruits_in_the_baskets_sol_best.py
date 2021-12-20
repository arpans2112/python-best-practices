class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        ret = 0
        prev = -1
        cur = fruits[0]
        num_cur = 0
        num_total = 0

        for f in fruits:
            if f == cur:
                num_cur += 1
                num_total += 1
            elif f == prev:
                prev = cur
                cur = f
                num_cur = 1
                num_total += 1
            else:
                ret = max(num_total, ret)
                prev = cur
                cur = f
                num_total = num_cur + 1
                num_cur = 1

        return max(ret, num_total)