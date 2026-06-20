class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        h = 0
        for i in range(len(arr)-1,-1,-1):
            curr = arr[i]
            arr[i]=h
            h = max(h,curr)
        arr[-1]=-1    
        return arr    
            


        
        