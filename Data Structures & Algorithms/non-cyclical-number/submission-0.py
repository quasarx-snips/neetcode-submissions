class Solution:
    def isHappy(self, n: int,h=None) -> bool:
        if h is None:
            h=set()
        s = 0
        for i in str(n):
            s+=int(i)**2

        if s==1:
            return True
        elif s in h:
            return False
        else:
            h.add(s)
            n=s     
            return self.isHappy(n,h)      

        