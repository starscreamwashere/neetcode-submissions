class Solution:
    def mySqrt(self, x: int) -> int:
        half=x//2
        if x==1 or x==0:
            return x
        if x==2 or x==3:
            return 1
        for i in range(0,half):
            if i*i>x:
                return i-1
            elif i*i==x:
                return i
        
        