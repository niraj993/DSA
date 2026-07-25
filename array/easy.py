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

# Right Rotate a one place
# Bute Force Solution
def right_rotate_one_place_brute(nums:List[int])->List[int]:
    last_ele = nums.pop()
    nums.insert(0,last_ele)
    return nums

# Better Solution
def right_rotate_one_place_better(nums:List[int])->List[int]:
    nums[:] = [nums[-1]] + nums[:-1]
    return nums


# Using Loop Solution
def right_rotate_one_place(nums:List)->List[int]:
    n = len(nums)
    last_ele = nums[-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = last_ele
    return nums 


# Right Rotate array by k place
# Brute Force Solution
def right_rotate_an_array_k_place_brute(nums:List[int],k:int)->List[int]:
    n = len(nums)
    if n == k:
        return nums
    rotation = k % n
    for i in range(rotation):
        last_ele = nums.pop()
        nums.insert(0,last_ele)
    return nums
    

# Better Solution Using the Slicing
def right_rotate_an_array_k_place_better(nums:List[int],k:int)->List[int]:
    n = len(nums)
    rotations = k % n
    nums[:] = nums[n-rotations:] + nums[:n-rotations]
    return nums



# Brute Force Using Dict
def move_zero_in_end_brute_force(nums:List[int])->List[int]:
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        if nums[i] != 0:
            freq_map[nums[i]] = 0
    
    index = 0
    for key in freq_map:
        nums[index] = key
        index +=1
    
    for j in range(index,n):
        nums[j] = 0
    return nums

    
# Better Solution  
def move_zero_in_end_better_solution(nums:List[int])->List[int]:
    n = len(nums)
    zeros = []
    non_zeros = []
    for i in range(0,n):
        if nums[i] == 0:
            zeros.append(nums[i])
        else:
            non_zeros.append(nums[i])
    nums[:] = non_zeros + zeros
    return nums


# Optimal Solution
def move_zero_in_end_optimal_solution(nums:List[int])->List[int]:
    n = len(nums)
    if n == 1:
        return 
    i = 0
    while i < n:
        if nums[i] != 0:
            break
        i+=1
    
    if i == n:
        return 
    j = i + 1
    while j < n:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
        j+=1
    return nums 


def linear_search(nums:List[int],target:int)->int:
    n = len(nums)
    for i in range(0,n):
        if nums[i] == target:
            return i
    return -1

def merge_two_sorted_an_array(nums1:List[int],nums2:List[int])->List[int]:
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    result = []
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j+=1

    while i < n:
        if len(result) == 0 or result[-1] != nums2[i]:
            result.append(nums1[i])
        i+=1

    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j+=1

    return result
    
  
# Brute Forec Solution 
def find_missing_num_in_an_array(nums:List[int])->int:
    n = len(nums)
    for i in range(1,n+1):
        if i not in nums:
            return i 
    return -1

# Bettel Solution
def find_missing_num_in_an_array_better(nums:List[int])->int:
    n = len(nums)
    freq_map = {}
    for i in range(1,n+1):
        freq_map[i] = 0
    
    for n in nums:
        if n in freq_map:
            freq_map[n] = 1

    for key in freq_map:
        if freq_map[key] == 0:
            return key

# Optimal solution
def find_missing_num_in_an_array_optimal(nums:List[int])->int:
    n = len(nums)
    return int((n * (n+1) // 2) - sum(nums))


# optimal solution
def max_consective_ones(nums:List[int])->int:
    n = len(nums)
    count = 0
    max_count = float("-inf")
    for i in range(0,n):
        if nums[i] == 1:
            count+=1
           
        else:
            max_count = max(count,max_count)
            count = 0
    return max(count,max_count)



result = max_consective_ones(nums=[1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0])
print("===============>",result)