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

 

def generate_subsequence_with_target_and_return_true_false(
    index: int,
    nums: List[int],
    subset: List[int],
    target: int,
    total: int
) -> bool:

    if total == target:
        return True

    if total > target or index >= len(nums):
        return False

    # Pick current element
    subset.append(nums[index])
    if generate_subsequence_with_target_and_return_true_false(
        index + 1, nums, subset, target, total + nums[index]
    ):
        return True

    # Not pick current element
    subset.pop()
    if generate_subsequence_with_target_and_return_true_false(
        index + 1, nums, subset, target, total
    ):
        return True

    return False

 

def generate_sub_seq_and_count(index: int, total: int, nums: List[int], k: int) -> int:
    # If all elements are processed
    if index == len(nums):
        return 1 if total == k else 0

    # Pick current element
    pick = generate_sub_seq_and_count(
        index + 1,
        total + nums[index],
        nums,
        k
    )

    # Do not pick current element
    not_pick = generate_sub_seq_and_count(
        index + 1,
        total,
        nums,
        k
    )

    return pick + not_pick


nums = [1, 2, 1]
k = 2

result = generate_sub_seq_and_count(0, 0, nums, k)
print(result)  # Output: 2

 