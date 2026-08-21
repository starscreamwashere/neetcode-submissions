import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap=[]
    for num in nums:
        pair=(-num,num)
        heapq.heappush(heap,pair)
    reverse_sorted=[]
    while heap:
        pair=heapq.heappop(heap)
        original_num=pair[1]
        reverse_sorted.append(original_num)



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
