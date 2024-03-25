# N - 나무의 수
# M - 집으로 가져가려고 하는 나무의 길이

# 적어도 M미터의 나무를 집에 가져가기 위한 절단기 높이의 최대값.

N, M = map(int, input().split())

trees = [i for i in map(int, input().split())]

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    # 가져갈 나무의 양
    get = 0
    for tree in trees:
        if tree > mid:
            get += tree - mid
    if get < M: # 최소값보다 작으면?
        end = mid - 1 # 좀 덜 잘라야겠다
    else:
        start = mid + 1 # 더 잘라도 되겠다

print(end)