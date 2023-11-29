# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        numbers = "0123456789"
        res = ""
        for e in s:
            if e in ["+", "-"]:
                res += e
                s = s[1:]
                break
            else:
                break

        i = 0
        any_digit = False
        while i < len(s) and s[i] in numbers:
            res += s[i]
            i += 1
            any_digit = True

        if not any_digit:
            return int(res + "0")

        res = int(res)

        if res <= -(2**31):
            return -(2**31)
        elif res >= 2**31 - 1:
            return 2**31 - 1

        return res


s2 = "words and 987"

s = Solution()
print("result:", s.myAtoi(s2))
