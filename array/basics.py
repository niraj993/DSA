def find_length_of_an_list(nums:List[int])->int:
    count = 0
    for _ in nums:
        count+=1
    return count

def find_max_element_in_array(nums:List[int])->int:
    max_elem = float("-inf")
    for ele in nums:
        max_elem = max(ele,max_elem)
    return max_elem

def find_min_element_in_array(nums:List[int])->int:
    min_ele = float("inf")
    for ele in nums:
        min_ele = min(min_ele,ele)
    return min_ele

def find_sum_of_all_ele(nums:List[int])->int:
    result = 0
    for ele in nums:
        result+=ele
    return result

def find_avg_of_an_array(nums:List[int])->int:
    count = 0
    asum = 0
    for ele in nums:
        count +=1
        asum+=ele
    return asum/count

def reverse_a_list(nums:List[int])->List[int]:
    result = []
    n = len(nums)
    for i in range(n-1,-1,-1):
        result.append(nums[i])
    return result

def sort_list_in_ascending_order(nums:List[int]):
    result = []
    n = len(nums)
    for i in range(0,n):
        for j in range(0,n):
            if nums[i] < nums[j]:
                result.append(nums[i])
    return result
result = sort_list_in_ascending_order(nums=[6,4,3,10,3,50])
print("===============>",result)