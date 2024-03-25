cnt = int(input())
print(2 ** cnt - 1)

def hanoi(n, fr, via, to):
    if n > 20:
        return

    if n == 1:
        print('{} {}'.format(fr, to))
    else:
        hanoi(n - 1, fr, to, via)
        print('{} {}'.format(fr, to))
        hanoi(n - 1, via, fr, to)

hanoi(cnt, 1, 2, 3)