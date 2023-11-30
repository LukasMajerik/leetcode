# https://leetcode.com/problems/palindrome-number/

import math


class Solution:
    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        modulo_res = None
        modulo_num = 1
        modulo_len = 0
        modulo_res = x % modulo_num
        while not modulo_res == x:
            modulo_num *= 10
            modulo_res = x % modulo_num
            modulo_len += 1

        # print("modulo_num:", modulo_num)
        # print("modulo_len:", modulo_len)

        num_is_odd = False
        if modulo_len % 2 != 0:
            num_is_odd = True
        # print("num_is_odd:", num_is_odd)
        half = 10 ** (int(modulo_len / 2))
        # print("half:", half)
        num_right_half = x % half
        # print("num_right_half:", num_right_half)
        num_left_half = x - num_right_half
        # print("num_left_half:", num_left_half)
        num_left_half_without_zeroes = num_left_half / half
        # print("num_left_half_without_zeroes:", num_left_half_without_zeroes)

        if num_is_odd:
            num_left_half_without_zeroes = int(num_left_half_without_zeroes / 10)

        # print("num_left_half_without_zeroes:", num_left_half_without_zeroes)

        num_right_half_reversed = 0

        for i in range(int(modulo_len / 2)):
            # print("num_right_half % 10:", num_right_half % 10)
            # print(
            #     "10 ** ((modulo_len / 2) - i):", 10 ** (int((modulo_len / 2)) - i - 1)
            # )

            num_right_half_reversed += (num_right_half % 10) * 10 ** (
                int((modulo_len / 2)) - i - 1
            )
            num_right_half = int(num_right_half / 10)
            # print("num_right_half_reversed:", num_right_half_reversed)

        # solve odd number

        return num_left_half_without_zeroes == num_right_half_reversed


s = Solution()
print(s.isPalindrome(246642))
# print(s.isPalindrome(13531))
