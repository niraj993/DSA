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
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# Brute Force Solution
def maximum_subarray_sum(nums:List[int])->int:
    n = len(nums)
    maxi_sum = float("-inf")
    for i in range(0,n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum+=nums[j]
            maxi_sum = max(maxi_sum,curr_sum)
    return maxi_sum

# Optimal Solution using the kadne's algorithem
def maximum_subarray_sum_optimal(nums:List[int])->int:
    n = len(nums)
    maxi = float("-inf")
    curr_sum = 0
    for i in range(0,n):
        curr_sum += nums[i]
        maxi = max(maxi,curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return maxi


# Brute Force Solution
def majority_element_n_by_2_brute(nums:List[int])->int:
    n = len(nums)
    for i in range(0,n):
        count = 0
        for j in range(0,n):
            if nums[i] == nums[j]:
                count+=1
        if count > n//2:
            return nums[i]
    



# Better  Solution
def majority_element_n_by_2(nums:List[int])->int:
    freq_map = {}
    n = len(nums)
    for i in range(0,n):
        freq_map[nums[i]] = freq_map.get(nums[i],0) + 1
 
    for key in freq_map:
        if freq_map[key] > n // 2:
            return key
    return -1
    
        

result = majority_element_n_by_2_brute(nums=[2,5,6,7,5,5,9,5,5])
print("==============>",result)