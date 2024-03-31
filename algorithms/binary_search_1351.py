class Solution(object):
    # generic binary search
    def binary_search(self, nums, lo, hi, condition):
        count = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            result = condition(mid)

            if result == 'left':
                count += 1
                hi = mid - 1
            elif result == 'right':
                lo = mid + 1

        return count
            
    # function to check if negative numbers exist
    def does_exist(self, nums):
        def condition(mid):
            mid_number = nums[mid]

            if mid_number < 0:
                if mid > 0 and nums[mid - 1] < 0:
                    return 'left'
                else:
                    return 'right'
            elif mid_number > 0:
                return 'right'
            
        return self.binary_search(nums, 0, len(nums) - 1, condition)

# Test cases
# arr = [[3, 2, 1, -1], [-1, -2, -3, -4]]
