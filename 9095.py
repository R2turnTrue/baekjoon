T = int(input())

for _ in range(T):
    N = int(input())
    
    dp = [-1] * 12

    def letsgo(n):
        if dp[n] == -1:
            if n == 0:
                dp[n] = 0
            elif n == 1:
                #1
                dp[n] = 1
            elif n == 2:
                #2
                #1+1
                dp[n] = 2
            elif n == 3:
                #1 + 1 + 1
                #1 + 2
                #2 + 1
                #3
                dp[n] = 4
            else:
                dp[n] = letsgo(n - 3) + letsgo(n - 2) + letsgo(n - 1)
        
        return dp[n]
    
    letsgo(N)
    print(dp[N])