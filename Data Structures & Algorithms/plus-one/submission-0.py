class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        faceValue=len(digits)-1
        num=0
        for digit in digits:
            num+=digit*(10**faceValue)
            faceValue-=1
        num+=1
        #number is ready till here,now we have to add its digits in a list
        revList=[]
        temp=num
        while num>0:
            digit=num%10
            revList.append(digit)
            num//=10
        #so list of digits of newnumber is also ready but in reverse order,so we now reverse it
        finalList=[]
        while revList:
            item=revList.pop()
            finalList.append(item)
        return finalList

            


        