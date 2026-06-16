class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        l = [0]*len(nums)
        for i in nums:
            m=m*i if i!=0 else m*1
        count = nums.count(0)
        if nums.count(0)>1:
            return l
        elif nums.count(0)==1:
            l[nums.index(0)] = m
            return l
        else:
            for index, i in enumerate(nums):
                l[index] = m // i
            return l
                




           