class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return x
        temp=x
        place_value=int(math.log10(abs(x)))
        rev=0
        x=abs(x)
        while x>0:
            digit=x%10
            rev+=digit*(10**place_value)
            place_value-=1
            x//=10
        if temp<0:
            rev*=-1
        if rev<(-2**31) or rev >(2**31)-1:
            return 0
        return rev


        