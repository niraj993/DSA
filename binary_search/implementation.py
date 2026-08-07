from typing import List

def binary_search(nums:List[int],target:int)->int:
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(nums:List[int],low:int,high:int,target:int)->int:
    if low > high:
        return -1
    
    mid = (low + high)//2
    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        low = mid + 1
    
    else:
        high = mid - 1
    
    return binary_search_recursive(nums,low,high,target)

nums=[1,2,3,4,5,6,7]
n = len(nums)
result = binary_search_recursive(nums=nums,target=7,low=0,high=n-1)
print("=============>result",result)