N = int(input())

A = []
A.extend(map(int, input().split()))
A.sort()

M = int(input())

B = []
B.extend(map(int, input().split()))

for b in B:
    n = 0
    #if b in A:
    #    n += 1

    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == b:
            n = 1
            break
        elif A[mid] < b: # 중간값이 너무 작다..
            start = mid + 1
        else: # == A[mid] > b, 중간값이 너무 크다..
            end = mid - 1
    
    print(n)