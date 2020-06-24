class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # we create a dictionary from each element in nums with keys being the element and value to be index
        num_keys = {val: index for index, val in enumerate(nums)}

        # we loop through nums array and check if target - current num is in dictionary
        for index in range(len(nums)):

            value_wanted = target - nums[index]

            # if value wanted is in dictionary and it's not value at given index
            if value_wanted in num_keys and index != num_keys[value_wanted]:

                # output asks for list with index of values that have sum of target
                return [index, num_keys[value_wanted]]
