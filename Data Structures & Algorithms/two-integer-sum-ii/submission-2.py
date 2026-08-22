class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexList=[]
        L=0
        R=len(numbers)-1
        while L<R:
            if(numbers[L]+numbers[R]==target):
                indexList.append(L+1)
                indexList.append(L+2)
                return indexList
            elif(numbers[L]+numbers[R]>target):
                R-=1
            else:
                L+=1
                
        