# https://leetcode.com/problems/remove-element/

EMPTY_VALUE = "_"


class Solution(object):
    def __init__(self):
        self.nums = []

    def __repr__(self):
        return str(self.nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        non_empty = 0
        _max = max([0, 1, 2, 2, 3, 0, 4, 2])
        _max_plus_1 = _max + 1

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = _max_plus_1

        nums.sort()

        for i in range(len(nums)):
            if nums[i] == _max_plus_1:
                nums[i] = EMPTY_VALUE
                non_empty += 1

        self.nums = nums

        return len(nums) - non_empty


s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(s)
