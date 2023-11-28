# https://leetcode.com/problems/median-of-two-sorted-arrays/


from typing import List
from statistics import median


class Solution:
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1 + nums2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            i = int(len(nums) / 2 - 1)
            j = int(len(nums) / 2)
            print(nums[i], nums[j])
            _median = (nums[i] + nums[j]) / 2
        else:
            i = int(len(nums) / 2 - 0.5)
            _median = nums[i]
        return _median


nums1 = [1, 3]
nums2 = [2]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
