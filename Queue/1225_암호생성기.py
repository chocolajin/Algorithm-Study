for tc in range(1,11):
    T = int(input())
    Q = list(map(int,input().split()))
    N = len(Q)

    minus = 1
    while Q[-1] > 0:
        num = Q.pop(0)
        num -= minus
        Q.append(num)

        minus += 1
        if minus == 6:
            minus = 1
    Q[-1]=0

    print(f'#{tc}', *Q)