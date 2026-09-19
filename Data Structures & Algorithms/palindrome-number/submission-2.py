class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        else:
            digits=int(math.log10(abs(x)))+1
            face_value=10**(digits-1)
            temp=x
            rev=0
            while x>0:
                curr=x%10
                rev+=curr*face_value
                face_value//=10
                x//=10
            if temp==rev:return True
            else:return False

        


        