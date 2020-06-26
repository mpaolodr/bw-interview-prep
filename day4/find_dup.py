"""
Wrong solution

modified array by sorting
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_check = 0
        for num in sorted(nums):

            if num_check == 0:

                num_check = num

            else:

                if num_check - num == 0:

                    return num

                else:

                    num_check = num
