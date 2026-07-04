from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    flag=0
    for i,n in enumerate(nums):
        if(n==7):
            flag=flag+1
            return i
    if(flag==0):
        return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_idx = None
    
    for i, n in enumerate(nums):
        if n == 7:
            if first_idx is None:
                # Store the index of the first '7' we find
                first_idx = i
            else:
                # We found the second '7', return the distance
                return i - first_idx



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
