class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Hash Map to store: element -> next greater element
        next_greater = {}
        stack = []

        # Process nums2 to build the mapping
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            stack.append(num)

        # Build answer for nums1 using the map
        return [next_greater.get(x, -1) for x in nums1]