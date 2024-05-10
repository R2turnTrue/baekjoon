# Without DP
"""
N = int(input())

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

print(fib(N))
"""

"""
# With DP (Bottom-up)
N = int(input())
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
"""

# With DP (Top-down)
N = int(input())
dp = [-1] * (N + 1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if dp[n] == -1:
        dp[n] = fib(n - 2) + fib(n - 1)

    return dp[n]

print(fib(N))