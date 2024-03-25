K, N = map(int, input().split())

cables = [int(input()) for i in range(K)]

start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2

    cnt = 0

    for cable in cables:
        cnt += cable // mid
    
    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1

print(start - 1)