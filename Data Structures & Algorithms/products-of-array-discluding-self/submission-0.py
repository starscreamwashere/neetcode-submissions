class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list=[]
        product=1
        product2=1
        for num in nums:
            product*=num
        for num in nums:
            if(num==0):
                for num2 in nums:
                    if num2!=0:
                        product2*=num2
                    else:
                        continue
                product_list.append(product2)#edgecase here is that what if num is zero,there your logic falls flat
            else:
                product_list.append(product/num)
        product_list=[int(x) for x in product_list]
        return product_list

        