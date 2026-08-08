from typing import List,Tuple

def three_sum_problme_brute_force(nums:List[int])->List[int]:
    n = len(nums)
    result = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = sorted([nums[i] , nums[j] , nums[k]])
                    result.add(tuple(temp))
    return [list(ele) for ele in result]


# Better Solution
def three_sum_problem_better(nums:List[int])->List[int]:
    n = len(nums)
    result = set()
    for i in range(0,n):
        my_set = set()
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in my_set:
                temp = [nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
    return [list(ans) for ans in result]

# Brute Force
def longest_subarray_equal_two_zero(nums:List[int])->int:
    n = len(nums)
    maxi = 0
    for i in range(0,n):
        result = 0
        for j in range(i,n):
            result += nums[j]
            if result == 0:
                maxi = max(maxi,j-i+1)
    return maxi


# Optimal Solution
def longest_subarray_equal_two_zero_optimal(nums:List[int])->int:
    n = len(nums)
    prefix_sum = {}
    maxi = 0
    sum_ = 0
    for i in range(0,n):
        sum_ += nums[i]
        if sum_ == 0:
            maxi = i + 1
        else:
            if sum_ in prefix_sum:
                maxi = max(maxi,i - prefix_sum[sum_])
            else:
                prefix_sum[sum_] = i
    return maxi


# Brute Force
def merge_two_sorted_an_array(nums_1:List[int],nums_2:List[int])->List[int]:
    result = []
    n = len(nums_1)
    m = len(nums_2)
    i = 0
    j = 0
    while i < n and j < m:
        if nums_1[i] < nums_2[j]:
            if len(result) == 0 or result[-1] != nums_1[i]:
                result.append(nums_1[i])
            i+=1
        else:
            if len(result) == 0 or result[-1] != nums_2[j]:
                result.append(nums_2[j])
            j+=1

    while i < n:
        if len(result) == 0 or result[-1] != nums_1[i]:
            result.append(nums_1[i])
        i+=1

    while j < m:
        if len(result) == 0 or result[-1] != nums_2[j]:
            result.append(nums_2[j])
        j+=1

    for i in range(len(result)):
        if i < n:
            nums_1[i] = result[i]
        else:
            nums_2[i-n] = result[i]

    print("=========>",nums_1)
    print("=========>",nums_2)

    return result


# Optimal Solution
def merge_two_sorted_an_array_optimal(nums1:List[int],nums2:List[int])->List[int]:
    n = len(nums1)
    m = len(nums2)
    i = n-1
    j = 0
    while i >= 0 and j < m:
        if nums1[i] > nums2[j]:
            nums2[j],nums1[i] = nums1[i],nums2[j]
        i-=1
        j+=1
    nums1.sort()
    nums2.sort()
    print("===========>",nums1)
    print("==========>",nums2)


# Brute Force
def find_missing_and_dupli_brute_force(nums:List[int])->int:
    n = len(nums)
    duplicate = None
    missing = None
    for i in range(1,n+1):
        if i not in nums:
            missing = i
    freq_map = {}
    for i in range(1,n):
        freq_map[nums[i]] = freq_map.get(nums[i],0) + 1

    for key in freq_map:
        if freq_map[key] == 2:
            duplicate = key

    return (missing,duplicate)


def find_missing_and_dupli_better(nums:List[int])->Tuple:
    n = len(nums)
    duplicate = -1
    missing = -1
    freq_map = {}
    for n in nums:
        freq_map[n] = freq_map.get(n,0) + 1

    for i in range(1,n+1):
        if i not in freq_map:
            missing = i
        elif freq_map[i] == 2:
            duplicate = i

        if missing != -1 and duplicate != -1:
            return (missing,duplicate)

        

# Optimal Solution
def find_missing_and_dupli_optimal(nums:List[int])->Tuple:
    pass

 


result = find_missing_and_dupli_better(nums=[1, 2, 2, 4])
print("====================>result",result)

