class Solution:

    def maxDifference(self, s: str) -> int:
        map = {}
        for char in s:
            map[char] = map.get(char, 0) + 1

        freqs = map.values()
        max_odd = max(f for f in freqs if f % 2 != 0)
        min_even = min(f for f in freqs if f % 2 == 0)

        return max_odd - min_even