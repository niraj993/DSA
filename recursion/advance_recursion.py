from typing import List

class Solution:
    def solve(self, index: int, subset: List[int], nums: List[int], result: List[List[int]]):
        # Base case: We've processed all elements, add current subset to result
        if index >= len(nums):
            result.append(subset.copy())  # Use copy to avoid modifying later
            return
        
        # Choice 1: Include the current element in the subset
        subset.append(nums[index])    # Add to current subset
        self.solve(index + 1, subset, nums, result)  # Recurse to next index
        
        # Backtrack: Undo the inclusion to try the exclude choice
        subset.pop()                  # Remove the last added element
        
        # Choice 2: Exclude the current element
        self.solve(index + 1, subset, nums, result)  # Recurse without adding

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []                   # List to store all subsets
        self.solve(0, [], nums, result)  # Start from index 0 with empty subset
        return result