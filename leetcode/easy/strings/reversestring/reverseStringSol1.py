class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while(i < len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            i+=1