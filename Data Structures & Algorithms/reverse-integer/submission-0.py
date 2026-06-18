class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        reversed_val = int(str(abs(x))[::-1])*sign
        return reversed_val if -2**31 <= reversed_val <= 2**31 - 1 else 0
  
        
        