import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    cmd = input()
    args = cmd.split()[1:]

    if cmd.startswith('push'):
        arr.append(args[0])
    elif cmd.startswith('pop'):
        if len(arr) < 1:
            print("-1")
        else:
            print(arr.pop())
    elif cmd.startswith('size'):
        print(len(arr))
    elif cmd.startswith('empty'):
        if len(arr) < 1:
            print('1')
        else:
            print('0')
    elif cmd.startswith('top'):
        if len(arr) < 1:
            print("-1")
        else:
            print(arr[-1])