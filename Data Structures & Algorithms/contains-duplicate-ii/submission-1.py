class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left=0
        right=k
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
                while len(window)>k:
                    window.remove(nums[i-k])
        return False            



        