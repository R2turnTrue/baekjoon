while True:
    num = str(int(input()))

    if num == '0':
        break

    l = (len(num) - 1) // 2

    if len(num) % 2 == 0:
        if num[:l+1] == ''.join(reversed(num[l+1:])):
            print('yes')
        else:
            print('no')
    elif num[:l] == ''.join(reversed(num[l+1:l*2+1])):
        print('yes')
    else:
        print('no')