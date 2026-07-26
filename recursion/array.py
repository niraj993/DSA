from typing import List

def find_sum_of_element(nums:List[int],count:int)->int:
    if count == len(nums):
        return 0
 
    return nums[count] + find_sum_of_element(nums,count+1)

def find_max_element_in_array(nums:List[int],count:int)->int:
    



result = find_sum_of_element(nums=[10,20,30,40],count=0)
print("==============>",result)