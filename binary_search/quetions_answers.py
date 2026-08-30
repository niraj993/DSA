from typing import List

# Brute Force
def search_insert_position_brute(nums:List[int],target:int)->int:
    n = len(nums)
    for i in range(0,n):
        if nums[i] >= target:
            return i
    return n


# Optimal
def search_insert_position(nums:List[int],target:int)->int:
    n = len(nums)
    low = 0
    high = n-1
    upper_bound = n
    while low <= high:
        mid = (low+high)//2
       
        if nums[mid] >= target:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    return upper_bound 


def find_floor_and_ceil(nums:List[int],target:int)->List[int]:
    n = len(nums)
    low = 0
    high = n-1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return [nums[mid],nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor,ceil]

# Brute Force
def find_first_and_last_occrance(nums:List[int],target:int)->List[int]:
    n = len(nums)
    first = -1
    last = -1
    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first,last]

# Optimal Solution
def find_first_and_last_occrance_optimal(nums:List[int],target:int)->List[int]:
    n = len(nums)
    low = 0
    high = n -1
    first = -1
    last = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            first = mid
            high = mid - 1
        else:
            last = mid
            low = mid + 1
    return [first,last]


result = find_first_and_last_occrance_optimal(nums=[1,2,3,3,3,3,3,4,5,6,7],target=3)
print("=========>",result)