"""
Wrong solution
- no need to read code

"""


def find_pivot(arr):

    if len(arr) == 0:
        return None

    elif len(arr) == 1:
        return 0

    elif len(arr) == 2:

        if arr[0] > arr[1]:
            return 1
        else:
            return 0

    elif len(arr) == 3:

        start = 0
        mid = start + 1
        end = start + 2

        if arr[start] < arr[mid]:
            return start

        elif arr[start] > arr[mid] and arr[mid] < arr[end]:
            return mid

    else:

        start = 0
        mid = start + 1
        end = start + 2

        while end != len(arr) - 1:

            if arr[end] < arr[mid]:

                return end

            elif arr[end] > arr[mid] and arr[start] > arr[mid]:

                return mid

            elif arr[start] < arr[mid] and arr[end] < arr[mid]:

                return end

            start += 1
            mid += 1
            end += 1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        pivot = find_pivot(nums)

        print(pivot)

        if pivot is None:
            return -1

        if pivot != 0 and len(nums) > 2:

            if target > nums[pivot]:

                if target < nums[pivot - 1]:

                    start = pivot

                    end = nums[pivot:][-1]

                    while start <= end:
                        mid = (start + end) // 2

                        if target < nums[mid]:

                            start = mid - 1

                        elif target > nums[mid]:
                            end = mid + 1

                        else:

                            return mid

                    return -1

                elif target > nums[pivot - 1]:

                    return -1

            elif target == nums[pivot]:

                return pivot

            else:

                return -1

        elif pivot == 0 and len(nums) > 2:

            low = 0
            high = len(nums) - 1

            while low <= high:

                mid = (low + high) // 2

                if target < nums[mid]:
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

                else:
                    return mid

            return -1

        elif pivot == 0 and len(nums) == 2:

            if target in nums:

                if target > nums[0]:
                    return 1
                else:
                    return 0

            else:
                return -1

        elif pivot == 1 and len(nums) == 2:

            if target in nums:

                if target > nums[pivot]:
                    return 0
                else:
                    return 1

            else:
                return -1

        elif pivot == 0 and len(nums) == 1:

            if target in nums:
                return 0
            else:
                return -1

        elif pivot == None:
            return -1
