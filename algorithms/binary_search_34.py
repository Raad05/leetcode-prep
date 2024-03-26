class Solution(object):
    def locate_number(self, nums, target, mid):
        mid_number = nums[mid]

        if mid_number == target:
            if mid - 1 >= 0 and nums[mid - 1] == target:
                return 'left'
            else:
                return 'found'
        elif mid_number > target:
            return 'left'
        elif mid_number < target:
            return 'right'

    def searchRange(self, nums, target):
        lo, hi = 0, len(nums) - 1
        output = [-1, -1]

        while lo <= hi:
            mid = (lo + hi) // 2
            result = locate_number(nums, target, mid)

            if result == 'found':
                output[0] = mid
                return
            elif result == 'left':
                hi = mid - 1
            elif result == 'right':
                lo = mid + 1
        