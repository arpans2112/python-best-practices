class Solution:
    def countAndSay(self, n: int) -> str:
        result = ["1"]
        i = 2
        while i <= n:
            result.append(self.say(result[i - 2]))
            i = i + 1
        return result[-1]

    def say(self, num: str) -> str:
        current = None
        count = 0
        output = ""
        for ch in num:
            if current != ch:
                if current:
                    output += f"{count}{current}"
                current = ch
                count = 1
            else:
                count = count + 1
        output += f"{count}{current}"
        return output