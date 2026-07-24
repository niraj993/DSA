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

# Optimal Solution
def find_second_element_optimal(nums:List[int])->int:
    largest = float("-inf")
    sec_largest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest and nums[i] != largest:
            sec_largest = largest
            largest = nums[i]
    return sec_largest


# Optimal Solution
def check_array_sorted_or_not(nums:List[int])->bool:
    n = len(nums)
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True

# Remove Duplicate from the sorted an array in place
# Brute Force
def remove_duplicate_from_sorted_an_array_brute(nums:List[int])->int:
    n = len(nums)
    result = []
    for i in range(0,n):
        if nums[i] not in result:
            result.append(nums[i])
    index = 0
    for j in range(0,len(result)):
        nums[index] = result[index]
        index +=1
   
    for k in range(len(result),n):
        nums[k] = 0
    
    return nums

# Better Solution
def remove_duplicate_from_sorted_an_array_better(nums:List[int])->int:
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        freq_map[nums[i]] = freq_map.get(nums[i],0) + 1

    index = 0
    for key in freq_map:
        nums[index] = key
        index+=1
    return nums

# Optimal Solution
def remove_duplicate_from_sorted_an_array_optimal(nums:List[int])->int:
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n :
        if nums[i] != nums[j]:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
      
        j+=1
    return i+1


    



result = remove_duplicate_from_sorted_an_array_better(nums=[1,1,1,2,3,4,5,6,2])
print("===============>",result)