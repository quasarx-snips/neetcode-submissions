class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area_list = []
        left = 0
        right = len(heights)-1
        area = 0
        while left<right:
            area = (right - left) * min(heights[left], heights[right]) if (right - left) * min(heights[left], heights[right])>area else area  
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1    
            

        return area    

        