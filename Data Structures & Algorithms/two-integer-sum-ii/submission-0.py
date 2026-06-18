class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i,val in enumerate(numbers):
            partner = target - val
            if val in hash:
                return [hash[val]+1,i+1]
            else:
                hash[partner]=i     
        