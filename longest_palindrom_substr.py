# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ""
        l = len(s)
        for i in range(l,0,-1):
            for j in range(0, i):
                # print(i, j)
                curr_str = s[j : i + 1]
                # print(curr_str)
                if self._is_palindrome(curr_str):
                    if len(curr_str) > len(longest_pal):
                        longest_pal = curr_str
                    if i<len(longest_pal):
                        return longest_pal

        return longest_pal

    def _is_palindrome(self, s):
        # if strings equals in normal and reversed orientation
        if s == (s)[::-1]:
            return True
        return False


s = Solution()
print(f"longest palindrome is: '{s.longestPalindrome("cbbd")}'")


# print(55*"*")
# for i in range(10,0,-1):
#     for j in range(i, 0, -1):
#         print(j)
