
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
            


# Brute Force
def fruit_in_buckets(nums:List[int]):
    max_length = 0
    n = len(nums)
    for i in range(0,n):
        my_set = set()
        for j in range(i,n):
            if len(my_set) > 2:
                break
            max_length = max(max_length,j-i+1)
    return max_length



def maximum_point_obtain(nums:List[int],k:int)->int:
    if k == len(cardPoints):
        return sum(cardPoints)

    max_sum = 0
    left_sum = 0
    right_sum = 0
    n = len(nums)
    # Take all k from the left initially
    for i in range(k):
        left_sum += nums[i]
    max_sum = left_sum

    # Slide: give back from left, take from right
    right_index = n - 1
    for i in range(k - 1, -1, -1):
        left_sum -= nums[i]          # remove one from the left window
        right_sum += nums[right_index]  # add one from the right tail
        right_index -= 1
        max_sum = max(max_sum, left_sum + right_sum)
    return max_sum

# Brute Force
def binary_sub_array_with_sum_brute(nums:List[int],goal:int)->int:
    n = len(nums)
    count = 0
    for i in range(0,n):
        total = 0
        for j in range(i,n):
            total += nums[j]
            if total > goal:
                break
            if total == goal:
                count+=1
    return count


class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0:
            return 0
        count = 0
        n = len(nums)
        left = 0
        right = 0
        Sum = 0
        while right < n:
            Sum += nums[right]
            while Sum > goal:
                Sum -= nums[left]
                left += 1
            count = count + ((right - left) + 1)
            right += 1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.countSubArrayLessThanOrEqualToGoal(
            nums, goal
        ) - self.countSubArrayLessThanOrEqualToGoal(nums, goal - 1)

class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0:
            return 0
        count = 0
        n = len(nums)
        left = 0
        right = 0
        Sum = 0
        while right < n:
            # Add 1 if nums[right] is odd, else add 0
            Sum += nums[right] % 2
            # Shrink window until number of odds <= goal
            while Sum > goal:
                Sum -= nums[left] % 2
                left += 1
            # All subarrays ending at right and starting from [left..right] are valid
            count = count + ((right - left) + 1)
            right += 1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.countSubArrayLessThanOrEqualToGoal(
            nums, k
        ) - self.countSubArrayLessThanOrEqualToGoal(nums, k - 1)


# brute force
def kdistancechar(k:int,string:str)->int:
    n = len(string)
    maxi = 0
    for i in range(0,n):
        my_set = set()
        for j in range(i,n):
            my_set.add(string[j])
            if len(my_set) > k:
                break
            maxi = max(maxi,j-i+1)
    return maxi

# Better Solution
def kdistancechar_better(k:int,string:str)->int:
    n = len(string)
    right = 0
    left = 0
    maxi = 0
    my_dict = dict()
    while right < n:
        my_dict[string[right]] = my_dict.get(string[right],0) + 1
        while len(my_dict) > k:
            my_dict[string[left]] -=1
            if my_dict[string[left]] == 0:
                del my_dict[string[left]]
            left+=1
        maxi = max(maxi,right-left +1)
        right+=1
    return right


# Optimal Solution
def kdistancechar_optimal(k:int,string:str)->int:
    n = len(string)
    right = 0
    left = 0
    maxi = 0
    my_dict = dict()
    while right < n:
        my_dict[string[right]] = my_dict.get(string[right],0) + 1
        if len(my_dict) > k:
            my_dict[string[left]] -=1
            if my_dict[string[left]] == 0:
                del my_dict[string[left]]
            left+=1
        if len(my_dict) <= 2:
            maxi = max(maxi,right-left +1)
        right+=1
    return right



result = kdistancechar_better(k=2,string="aaabbccd")
print("============>",result)