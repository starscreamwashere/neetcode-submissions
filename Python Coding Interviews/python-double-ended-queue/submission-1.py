from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    rightRotatedQueue=deque(arr)
    flag=1
    length=len(rightRotatedQueue)
    while flag<=k:
        rightRotatedQueue.appendleft(rightRotatedQueue[length-1])
        flag=flag+1
    while k>0:
        rightRotatedQueue.pop()
        k=k-1
    return rightRotatedQueue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
