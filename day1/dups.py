class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # creating keys for element to eliminate duplication if any
        distinct = {num for num in nums}

        # check if they have same number of elements
        if len(distinct) == len(nums):
            return False
        else:
            return True
