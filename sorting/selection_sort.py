from typing import List


def selection_sort(nums:List[int])->List[int]:
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums



result = selection_sort(nums=[5,10,1,3,11,2])
print("====================>",result)