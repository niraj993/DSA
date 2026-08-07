from typing import List

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


result = three_sum_problem_better(nums=[-1,0,1,2,-1,-4])
print("====================>result",result)

