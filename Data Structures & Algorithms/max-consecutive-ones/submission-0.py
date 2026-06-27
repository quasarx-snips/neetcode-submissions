class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0 #current streak
        l=0 #longest streak
        for i in nums:
            if i==1:
                m+=1
                if m>l:
                    l=m 
            if i==0:
                m=0
                
        return l

        