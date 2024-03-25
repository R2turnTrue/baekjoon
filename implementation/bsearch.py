# 이진탐색

val = int(input())

arr = [1, 67, 24, 36, 12]
arr.sort()

first, last = 0, len(arr) - 1

while first <= last:
    mid = (first + last) // 2
    if arr[mid] == val:
        print(mid)
        break
    elif arr[mid] < val:
        first = mid + 1
    else:
        last = mid - 1