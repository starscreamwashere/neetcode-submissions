#i^2==x    2=math.log(x,i)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        if x==2 or x==3:
            return 1
        for i in range(2,x+1):
            sqrt=math.log(x,i)
            if sqrt<2:
                return i-1
        
        