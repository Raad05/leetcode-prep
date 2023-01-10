class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = -1
        for i in range(len(nums)):
            if (nums[i] == 1):
                c += 1
            else:
                res = max(res, c)
                c = 0
        res = max(res, c)
        return res
