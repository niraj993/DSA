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
    
        
# Optimal Solution Using the moorse voting algo
def moorse_voting_algo(nums:List[int])->int:
    n = len(nums)
    count = 0
    ele = None  
    for i in range(0,n):
        if count == 0:
            ele = nums[i]
            count+=1
        elif nums[i] == ele:
            count+=1
        else:
            count -= 1
    count = 0
    for i in range(0,n):
        if nums[i] == ele:
            count +=1
    
    if count > n//2:
        return ele
    else:
        return -1

# Brute Force Solution
def buy_and_sell(nums:List[int])->int:
    n = len(nums)
    maxi_profit = float("-inf")
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                profit = nums[j] - nums[i]
                maxi_profit = max(maxi_profit,profit)
    return maxi_profit

# Optimal Solution
def buy_and_sel_optimal(nums:List[int])->int:
    n = len(nums)
    min_price = float("inf")
    maxi_profit = float("-inf")
    for i in range(0,n):
        min_price = min(min_price,nums[i])
        profit = nums[i] - min_price
        maxi_profit = max(maxi_profit,profit)
    return maxi_profit

# Brute Force Solution
def rearrange_list_by_sign_brute_force(nums:List[int])->List[int]:
    n = len(nums)
    result = [0] * n
    pos = []
    neg = []
    for i in range(0,n):
        if nums[i] > 0 :
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    posindex = 0
    negindex = 1
    for i in range(0,len(pos)):
        result[posindex] = pos[i]
        posindex+=2
        result[negindex] = neg[i]
        negindex+=2
    return result

 

# Optimal Solution 
def rearrange_list_by_sign(nums:List[int])->List[int]:
    n = len(nums)
    result = [0] * n
    pos = 0
    neg = 1
    for i in range(0,n):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos += 2
        else:
            result[neg] = nums[i]
            neg+=2
    return result


# Brute Force Leaders in an array
def leaders_in_an_array_brute(nums:List[int])->List[int]:
    n = len(nums)
    result = []
    for i in range(0,n):
        is_leader = True
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                is_leader = False
                break

        if is_leader:
            result.append(nums[i])
    return result

# Optimal Solution Leaders in an array
def leaders_in_an_array_optimal(nums:List[int])->List[int]:
    n = len(nums)
    result = []
    maxi_ele = float("-inf")
    for i in range(n-1,-1,-1):
        ele = max(maxi_ele,nums[i])
        if ele > maxi_ele:
            result.append(ele)
            maxi_ele = ele
    return result[::-1]

# Brute force solution
def longest_consective_seq(nums:List[int])->int:
    n = len(nums)
    max_count = 0
    for i in range(0,n):
        ele = nums[i]
        count = 1
        n = ele
        while n + 1 in nums:
            count+=1
            n+=1
        max_count = max(max_count,count)
    return max_count


# Optimal Solution
def longest_consective_seq_optimal(nums: List[int]) -> int:
    my_set = set(nums)
    max_count = 0

    for ele in my_set:
        # Start only if ele is the first element of a sequence
        if ele - 1 not in my_set:
            count = 1
            current = ele

            while current + 1 in my_set:
                current += 1
                count += 1

            max_count = max(max_count, count)

    return max_count    





result = longest_consective_seq_optimal(nums=[1,99,101,98,2,5,3,100])
print("==============>",result)