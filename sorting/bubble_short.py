from typing import List

# Brute Force
def bubble_sort(nums:List[int])->List[int]:
    n = len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums


# Better Solution
def bubble_sort_better(nums:List[int])->List[int]:
    n = len(nums)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swap = True
        if is_swap == False:
            break
        
    return nums

result = bubble_sort(nums=[3,2,4,1,5,6,10,8])
print("============>",result)