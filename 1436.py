N = int(input())
res = 666
n = 0

while True:
    if '666' in str(res):
        n += 1

    if N == n:
        print(res)
        break

    res += 1