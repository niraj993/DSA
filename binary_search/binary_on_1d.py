from typing import List

def find_lower_bound(nums:List[int],target:int)->int:
    n = len(nums)
    low = 0
    high = n-1
    lower_bound = -1
    while high >= low:
        mid = (low + high)//2
        if nums[mid] >= target:
            lower_bound = mid
            high = mid -1
        else:
            low = mid + 1
    return lower_bound


def find_upper_bound(nums:List[int],target:int)->int:
    n = len(nums)
    upper_bound = n 
    low = 0
    high = n-1
    while high >= low:
        mid = (low + high)//2
        if nums[mid] <= target:
            upper_bound = mid
            low = mid + 1
        else:
            high = mid - 1 

    return upper_bound





result = find_upper_bound(nums=[1,1,1,2,3,4,5,6,6],target=1)
print("=============>result",result)