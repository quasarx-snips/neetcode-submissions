class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_a = sum(nums)
        sum_s = (len(nums)*(len(nums)+1))/2
        return int(sum_s)-sum_a 