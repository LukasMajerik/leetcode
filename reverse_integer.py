# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[::-1]
            x = x.replace("-", "")
            x = "-" + x
        else:
            x = str(x)[::-1]

        x = int(x)

        if not -(2**31) <= x <= 2**31 - 1:
            return 0

        return x


s = Solution()
print(s.reverse(1534236469))
