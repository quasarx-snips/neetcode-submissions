class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        win={}
        for i in nums:
            win[i]=nums.count(i)
        return sorted(win, key=win.get, reverse=True)[:k]    
        
