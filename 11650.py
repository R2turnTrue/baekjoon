import sys
input = sys.stdin.readline

N = int(input().strip())
arr = []

for i in range(N):
    arr.append(tuple(map(int, input().strip().split())))

arr.sort()

for i in arr:
    print(str(i).replace('(', '').replace(')', '').replace(',', ''))