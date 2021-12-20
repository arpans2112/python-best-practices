

class Solution:
    def reverse(self, x: int) -> int:
        newint = int(str(x)[::-1]) if x >= 0 else int(str(x)[::-1][:-1])*-1
        return  newint  if  -2**31 <= newint <= 2**31-1 else 0