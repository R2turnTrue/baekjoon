# 집의 갯수 - N
# 공유기의 갯수 - C

N, C = map(int, input().split())

houses = [int(input()) for i in range(N)]

houses.sort()

start = 1
end = houses[-1] - houses[0] # 끝집과 첫집 사이 거리
result = 0

# 이분탐색 - 적정 거리 찾기!

while start <= end:
    mid = (start + end) // 2 # 현재 공유기 거리

    current = houses[0]
    # 공유기 갯수
    cnt = 1

    # 얼마나 설치할 수 있을까..
    for i in range(1, len(houses)):
        house = houses[i]
        # 현재거리보다 넓게 있는가?
        if house >= current + mid:
            cnt += 1
            current = house
    
    # 목표수보다 많을때
    if cnt >= C:
        # 거리가 너무 좁아..
        # 최저 거리를 늘리자!
        start = mid + 1
        result = mid
    else: # 목표수보다 적을때
        # 거리가 너무 넓어..
        # 최대 거리를 줄이자!
        end = mid - 1

print(result)