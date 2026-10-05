#looking at the given examples , I am assuming that loop will stop when your sum of digits is a single digit number , if that single digit number is 1 , then true , else false
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        if n==1:
            return True
        sum=0
        while n>0:
            digit=n%10
            sum+=digit**2
            n//=10
            if n==0:
                n=sum
                if sum in seen:
                    return False
                seen.add(sum)
                if sum==1:
                    return True
                sum=0

        
            

        