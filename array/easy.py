from typing import List

# Brute Force Solution
def find_largest_ele(nums:List[int])->int:
    nums.sort()
    return nums[-1]

# Optimal Solution
def find_largest_ele_optimal(nums:List[int])->int:
    n = len(nums)
    largest_ele = float("-inf")
    for i in range(0,n):
        largest_ele = max(largest_ele,nums[i])
    return largest_ele
        

# Brute Force Solution
def find_second_largest_ele_brute(nums:List[int])->int:
    nums.sort()
    return nums[-2]



# Better Solution
def find_second_largest_ele_better(nums:List[int])->int:
    n = len(nums)
    largest_ele = float("-inf")
    second_largest = float("-inf")
    for i in range(0,n):
        if nums[i] > largest_ele:
            largest_ele = nums[i]
  
    for j in range(0,n):
        if nums[j] > second_largest and nums[j] != largest_ele:
            second_largest = nums[j]
    return second_largest


result = find_largest_ele_optimal(nums=[56,3,2,10,65,15])
print("===============>",result)