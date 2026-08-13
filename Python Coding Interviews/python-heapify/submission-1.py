import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings)
    heaped_strings=[]
    while strings:
        heaped_strings.append(heapq.heappop(strings))
    return heaped_strings


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    heaped_integers=[]
    while integers:
        heaped_integers.append(heapq.heappop(integers))
    return heaped_integers


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    heaped_nums=[]
    while nums:
        heaped_nums.append(heapq.heappop(nums))
    return heaped_nums


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
