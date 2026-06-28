class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        high_map = {}
        for org in range(len(nums2)):
            high = org + 1
            while high < len(nums2) and nums2[org] >= nums2[high]:
                high += 1
            if high < len(nums2) and nums2[org] < nums2[high]:
                high_map[nums2[org]] = nums2[high]
            else:
                high_map[nums2[org]] = -1
        return [high_map[num] for num in nums1]