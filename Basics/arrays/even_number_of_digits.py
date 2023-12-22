class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for item in nums:
            num = item
            c = 0
            while (num != 0):
                num = num // 10
                c += 1
            if (c % 2 == 0):
                res += 1
        return res
