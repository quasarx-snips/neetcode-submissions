class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        mins = strs[0]
        x = ""
        for i in strs:
            while not i.startswith(mins):
                mins = mins[:-1]
                if not mins:
                    return ""
        return mins    

               
         