from typing import List

def generate_subsequence(index: int, nums: List[int], subset: List[int], result: List[List[int]]) -> None:
    if index >= len(nums):
        result.append(subset.copy())
        return

    # Include current element
    subset.append(nums[index])
    generate_subsequence(index + 1, nums, subset, result)

    # Exclude current element
    subset.pop()
    generate_subsequence(index + 1, nums, subset, result)

 
# Brute Force
def generate_subsequence_with_target(index: int, nums: List[int], subset: List[int],
                                     result: List[List[int]], target: int) -> None:
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
        return

    # Include current element
    subset.append(nums[index])
    generate_subsequence_with_target(index + 1, nums, subset, result, target)

    # Exclude current element
    subset.pop()
    generate_subsequence_with_target(index + 1, nums, subset, result, target)


# Optimal Solution
def generate_subsequence_with_target_optimal(
    index: int,
    nums: List[int],
    subset: List[int],
    result: List[List[int]],
    target: int,
    total: int
) -> None:

    if total == target:
        result.append(subset.copy())
        return

    if total > target or index >= len(nums):
        return

    # Include current element
    subset.append(nums[index])
    generate_subsequence_with_target_optimal(
        index + 1, nums, subset, result, target, total + nums[index]
    )

    # Exclude current element
    subset.pop()
    generate_subsequence_with_target_optimal(
        index + 1, nums, subset, result, target, total
    )


nums = [1, 2, 3]
target = 3
result = []

generate_subsequence_with_target_optimal(0, nums, [], result, target, 0)

print(result)

                            
 

 