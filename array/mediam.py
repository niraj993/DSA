from typing import List

# Brute Force Approach
def two_sum(nums:List[int],target:int)->List[int]:
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [-1,-1]

# Optimal Approach
def two_sum_optimal(nums:List[int],target:int)->List[int]:
    n = len(nums)
    dict_map = {}
    for i in range(0,n):
        remain = target - nums[i]
        if remain in dict_map:
            return [dict_map[remain],i]
        dict_map[nums[i]] = i
    

# Sort Color on in-place brute force
# Time o(n log(n))
def sort_colour_brute(nums:List[int]):
    nums.sort()
    return nums

# better Solution 1
def sort_colour_better(nums:List[int])->List[int]:
    n = len(nums)
    zeros = []
    ones = []
    twos = []
    for i in range(0,n):
        if nums[i] == 0:
            zeros.append(nums[i])
        elif nums[i] == 1:
            ones.append(nums[i])
        else:
            twos.append(nums[i])
    nums[:] = zeros + ones + twos
    return nums

# Better Solution 2
def sort_colour_better_2(nums:List[int])->List[int]:
    n = len(nums)
    zeros = 0
    ones = 0
    twos = 0
    for i in range(0,n):
        if nums[i] == 0:
            zeros +=1
        elif nums[i] == 1:
            ones +=1
        else:
            twos+=1
    for i in range(0,zeros):
        nums[i] = 0
    for j in range(zeros,zeros+ones):
        nums[j] = 1
    for k in range(zeros+ones,n):
        nums[k] = 2
    
    return nums

# Dutch National Flag
def dutch_national_flag(nums:List[int])->List[int]:
    pass

    

result = sort_colour_better_2(nums=[1,0,2,0,2,1])
print("==============>",result)