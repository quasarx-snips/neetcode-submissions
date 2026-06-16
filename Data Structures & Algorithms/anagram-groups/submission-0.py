class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for i in strs:
            sign = "".join(sorted(i))
            hash[sign].append(i)
        return list(hash.values())    

            
        