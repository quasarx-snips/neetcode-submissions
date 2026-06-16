class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,val in enumerate(nums):
            partner = target-val
            if partner in hash:
                return [hash[partner],i]
            else:
                hash[val]=i      
        