class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        num=0
        face_value=1
        while x>0:
            digit=x%10
            num+=digit*face_value
            face_value*=10
            x//=10
        if num==temp:
            return True
        else:
            return False

        