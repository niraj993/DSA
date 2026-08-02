from typing import List


# using recursion
def climbing_stairs(n:int):
    if n == 1 or n == 0:
        return 1
    return climbing_stairs(n-1) + climbing_stairs(n-2)


# Recursion with memoization
def climbing_stairs_with_memo(n: int, dp: List[int]) -> int:
    if n == 0 or n == 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = (
        climbing_stairs_with_memo(n - 1, dp) +
        climbing_stairs_with_memo(n - 2, dp)
    )
    
    return dp[n]

# Climbing staires with tabulation
def climbing_stairs_with_tab(n:int):
    dp = [-1] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

 
def climbing_stairs_with_tab_space_optimization(n:int):
    prev2 = 1
    prev = 1
    for i in range(2,n+1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr
    return prev

 
# Using recursion Brute force
def jump_frog_brute(height, index):
    if index == 0:
        return 0

    jump1 = jump_frog(height, index - 1) + abs(height[index] - height[index - 1])

    if index > 1:
        jump2 = jump_frog(height, index - 2) + abs(
            height[index] - height[index - 2]
        )
    else:
        jump2 = float("inf")
    return min(jump1, jump2)


def jump_frog_using_memo(index:int,heights:List[int],dp:List[int])->int:
    if index == 0:
        return 0
    
    if dp[index] != -1:
        return dp[index]

    jump1 = jump_frog(height, index - 1) + abs(height[index] - height[index - 1])

    if index > 1:
        jump2 = jump_frog(height, index - 2) + abs(
            height[index] - height[index - 2]
        )
    else:
        jump2 = float("inf")
    dp[index] = min(jump1, jump2)

    return dp[index]

# Jump frog using tabulation
def jump_frog_using_tabulation(n:int,height:List[int])->int:
    dp = [-1] * (n)
    dp[0] = 0
    for index in range(1,n):
        jump1 = dp[index-1] + abs(height[index] - height[index - 1])
        if index > 1:
            jump2 = dp[index-2] + abs(height[index] - height[index - 2])
        else:
            jump2 = float("inf")
        
        dp[index] = min(jump1, jump2)
    return dp[n-1]
 
# Tabulation with space optimization
def jump_frog_space_optimized(n: int, height: List[int]) -> int:
    prev = 0      # dp[0]
    prev2 = 0     # dp[-1] (not used initially)

    for i in range(1, n):
        jump1 = prev + abs(height[i] - height[i - 1])

        if i > 1:
            jump2 = prev2 + abs(height[i] - height[i - 2])
        else:
            jump2 = float('inf')

        curr = min(jump1, jump2)

        # shift values for next iteration
        prev2 = prev
        prev = curr

    return prev
 

# using Recursion
def robber_1(index:int,nums:List[int])->int:
    if index == 0:
        return nums[0]
    
    if index < 0:
        return 0
    
    pick = nums[index] + robber_1(index-2,nums)
    not_pick = 0 +  robber_1(index-1,nums)
    return max(pick,not_pick)

# Using memoization
def robber_1_using_memo(index: int, nums: List[int], dp: List[int]) -> int:
    if index == 0:
        return nums[0]

    if index < 0:
        return 0

    # return already computed result
    if dp[index] != -1:
        return dp[index]

    pick = nums[index] + robber_1_using_memo(index - 2, nums, dp)
    not_pick = robber_1_using_memo(index - 1, nums, dp)

    dp[index] = max(pick, not_pick)
    return dp[index]


# using tabulation bottom-top apporoach
def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]

    for index in range(1, n):
        pick = nums[index]
        if index > 1:
            pick += dp[index - 2]

        not_pick = dp[index - 1]

        dp[index] = max(pick, not_pick)

    return dp[n - 1]

 

 
 
# tabulation with space optimized
def robber_space_optimized(nums: List[int]) -> int:
    n = len(nums)

    if n == 0:
        return 0

    prev = nums[0]   # dp[0]
    prev2 = 0        # dp[-1]

    for i in range(1, n):
        pick = nums[i] + prev2
        not_pick = prev

        curr = max(pick, not_pick)

        # shift for next iteration
        prev2 = prev
        prev = curr

    return prev


 

