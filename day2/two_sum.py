class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_keys = {val: index for index, val in enumerate(nums)}

        for index in range(len(nums)):

            value_wanted = target - nums[index]

            if value_wanted in num_keys and index != num_keys[value_wanted]:
                return [index, num_keys[value_wanted]]
