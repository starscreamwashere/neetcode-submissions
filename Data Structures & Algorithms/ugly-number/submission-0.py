class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        for i in range(2,n+1):
            if n%i!=0:
                continue
            else:
                primeCounter=0
                for j in range(1,i+1):
                    if i%j==0:
                        primeCounter+=1
                if primeCounter==2:
                    if i!=2 and i!=3 and i!=5:
                        return False
        return True

                    
        