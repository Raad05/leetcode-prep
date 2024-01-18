# recursive approach
def fib(num, dp):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif dp[num] != -1:
        return dp[num]
    
    dp[num] = fib(num - 1, dp) + fib(num - 2, dp)
    return dp[num]

dp = [-1] * 8
print(fib(7, dp))