
from typing import List

# Brute Force
def find_longest_sub_string(string:str)->int:
    n = len(string)
    maxi = 0
    for i in range(0,n):
        my_set = set()
        for j in range(i,n):
            if string[j] in my_set:
                break
            maxi = max(maxi,j-i+1)
            my_set.add(string[j])
    return maxi



# Optimal Solution
def find_longest_sub_string_optimal(string:str)->int:
    n = len(string)
    if n == 1:
        return 1
    left = 0
    right = 0
    freq_map = {}
    longest = 0
    while right < n:
        if string[right] in freq_map:
            left = max(left, freq_map[right] + 1)
        
        longest = max(longest,right-left+1)
        freq_map[right] = right
        right+=1
    return longest
            

# Brute Force 
def max_consective_ones_111(nums:List[int],k:int)->int:
    n = len(nums)
    maxi_ones = 0
    for i in range(0,n):
        count_zero = 0
        for j in range(i,n):
            if nums[j] == 0:
                count_zero+=1
            if count_zero > k:
                break
            maxi_ones = max(maxi_ones,j-i+1)
    return maxi_ones

# better Solution
def max_consective_ones_better_111(nums:List[int],k:int)->int:
    n = len(nums)
    left = 0
    right = 0
    maxi_ones = 0
    zeros_count = 0
    while right < n:
        if nums[right] == 0:
            zeros_count+=1
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left+=1
        if zeros_count <= k:
            maxi_ones = max(maxi_ones,right-left + 1)
        
        right+=1
    return maxi_ones
            
# Optimal Solution
def max_consective_ones_optimal_111(nums:List[int],k:int)->int:
    n = len(nums)
    left = 0
    right = 0
    maxi_ones = 0
    zeros_count = 0
    while right < n:
        if nums[right] == 0:
            zeros_count+=1
        if zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left+=1
        if zeros_count <= k:
            maxi_ones = max(maxi_ones,right-left + 1)
        
        right+=1
    return maxi_ones
            


# Brute Force
def fruit_in_buckets(nums:List[int])->int:
    n = len(nums)
    maxi = 0
    for i in range(0,n):
        my_set = set()
        for j in range(i,n):
            my_set.add(nums[j])
            if len(my_set) > 2:
                break
            maxi = max(maxi,j-i+1)
    return maxi

# Better Solution 
def fruit_in_buckets_better_solution(nums:List[int])->int:
    n = len(nums)
    right = 0
    left = 0
    freq_map = {}
    max_len = 0
    while right < n:
        freq_map[nums[right]] = freq_map.get(nums[right],0) + 1
        while len(freq_map) > 2:
            freq_map[nums[left]] -= 1
            if nums[left] == 0:
                del nums[left]
            left+=1

        if len(freq_map) <= 2:
            max_len = max(max_len,right-left+1)
        right+=1
    return max_len

# Optimal Solution
def fruit_in_buckets_optimal_solution(nums:List[int])->int:
    n = len(nums)
    left = 0
    right = 0
    max_len = 0
    freq_map = {}
    while right < n:
        freq_map[nums[right]] = freq_map.get(nums[right],0) + 1

        if len(freq_map) > 0:
            freq_map[nums[left]] -= 1
            if nums[left] == 0:
                del nums[left]
            left+=1
        if len(freq_map) <= 2:
            max_len = max(max_len,right-left+1)

        right+=1
    return max_len

        

# Brute Force
def maximum_point_obtain_brute_force(nums:List[int],k:int)->int:
    n = len(nums)
    maxi_point = 0
    for i in range(0,n):
        result = 0
        count = 0
        for j in range(i,n):
            result = result + nums[j]
            count+=1
            if count == k:
                maxi_point = max(maxi_point,result)
                break

    return maxi_point



# Optimal Solution
from typing import List

def maximum_point_obtain_optimal(nums: List[int], k: int) -> int:
    n = len(nums)
    if n == k:
        return sum(nums)

    left_sum = 0
    right_sum = 0

    for i in range(k):
        left_sum += nums[i]

    maxi = left_sum
    right_index = n - 1

    for i in range(k - 1, -1, -1):
        left_sum -= nums[i]
        right_sum += nums[right_index]
        maxi = max(maxi, left_sum + right_sum)
        right_index -= 1

    return maxi


def binary_sub_array_with_sum(nums: List[int], target: int) -> int:
    n = len(nums)
    for 

result = maximum_point_obtain_optimal([1, 2, 3, 4, 5, 6, 1], 3)
print("===========>", result)

    


 