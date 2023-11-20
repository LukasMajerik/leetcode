# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        return self.twoSumHashTable(nums, target)

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l_n = len(nums)

        for i in range(l_n):
            for j in range(l_n):
                if j != i:
                    if nums[i] + nums[j] == target:
                        return [i, j]

        return [None]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_result = self._sort_and_find(nums, target)

        idx_res_0 = int(nums.index(nums_result[0]))
        idx_res_1 = int(nums.index(nums_result[1]))

        if nums_result[0] != nums_result[1]:
            return [idx_res_0, idx_res_1]
        else:
            # if both nums are same num, find 2nd one
            idx_res_same_num_2nd = int(
                nums.index(nums_result[0], nums.index(nums_result[0]) + 1)
            )
            return [idx_res_0, idx_res_same_num_2nd]

    def _sort_and_find(self, nums, target):
        l_n = len(nums)
        nums_s = sorted(nums)

        j = 1

        for i in range(l_n):
            while j < l_n:
                if nums_s[i] + nums_s[j] == target:
                    return [nums_s[i], nums_s[j]]
                j += 1
            j = i + 2

        return [None]

    def twoSumHashTable(self, nums, target):
        l_n = len(nums)

        # hash table of value and it's index
        hash_tab = {}

        hash_tab.setdefault(nums[0], 0)

        for i in range(1, l_n):
            print(target, nums[i], target - nums[i])
            print(hash_tab)
            if target - nums[i] in hash_tab:
                print("I am in if", "i:", i, hash_tab[target - nums[i]])
                return [i, hash_tab[target - nums[i]]]
            hash_tab.setdefault(nums[i], i)

        return [None]


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
# print("result:", s.twoSum([2, 7, 15, -12, 3], 3))
# print(s.twoSum([1, 2, 3, 4, 5, -12, -15], 9))
print(s.twoSum([2, 5, 5, 11], 10))
# print(s.twoSum([3, 3], 6))


d = {2: 0, 7: 1, 11: 2, 15: 3}
if 6 in d:
    print("7 is there")
