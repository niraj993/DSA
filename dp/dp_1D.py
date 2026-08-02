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


result = climbing_stairs_with_tab_space_optimization(n=5)
print("==========result",result)

