
from typing import List

# Brute Force
def find_longest_sub_string(string:str)->int:
    n = len(string)
    longest = float("-inf")
    for i in range(0,n):
        my_set = set()
        count = 0
        for j in range(i,n):
            if string[j] in my_set:
                break
            my_set.add(string[j])
            longest = max(longest, j - i + 1)
    return longest
        

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
            left = max(left,freq_map[string[right]] + 1)
   
        longest = max(longest,right-left+1)
        freq_map[string[right]] = right
        right +=1
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
            


result = max_consective_ones_optimal_111(nums=[1,1,1,0,0,0,1,1,1,1,0,0,1,1],k=2)
print("============>",result)