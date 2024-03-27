N, K = map(int, input().split())

levels = [int(input()) for i in range(N)]

levels.sort()

first, last = levels[0], levels[-1] + K

def dif(mid):
    diff = 0
    for level in levels:
        if level < mid:
            diff += mid - level
        else:
            break
    return diff

while first <= last:
    # mid 레벨까지 올려야된다!
    mid = (first + last) // 2
    # mid 레벨까지 올리려면 얼마나?
    diff = dif(mid)

    if diff <= K: # 너무 작다!
        first = mid + 1 # 더 올려쳐도 될듯?
    else: # 너무 크다!
        last = mid - 1 # 좀만 작아지게..

print(last)