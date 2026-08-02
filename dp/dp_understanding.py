# Using recursion Fibnacci

# Top-down
def fib(nums:int)->int:
    if nums == 0:
        return 0
    
    if nums == 1:
        return 1

    return fib(nums-1) + fib(nums-2)



# Fibnacci with memoization dynamic programing
def fib_with_memo(n,dp):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_with_memo(n-1,dp) + fib_with_memo(n-2,dp)
    return dp[n]

n = 4
dp = [-1] * (n+1)

# bottom up solution
# Fib with tabulation
def fib_with_tabulation(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Tabulation of space otimization
def fib_tabu_space_opti(n:int)->int:
    prev2 = 0
    prev = 1
    for i in range(2,n+1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr
    return prev



result = fib_tabu_space_opti(n=3)
 
print("==========>",result)