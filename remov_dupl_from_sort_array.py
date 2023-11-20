# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

EMPTY_VALUE = "_"


class Solution(object):
    def __init__(self):
        self.nums = []

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        arr = []
        arr_empty = []

        curr = ""

        for e in nums:
            if e != curr:
                arr.append(e)
                curr = e
            else:
                arr_empty.append(EMPTY_VALUE)

        self.nums = arr + arr_empty

        return len(arr)

    def __repr__(self):
        return str(self.nums)


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s)
