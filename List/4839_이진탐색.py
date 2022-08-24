T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # print(P,Pa,Pb)

    def bS(N, key):
        l = 1
        r = N
        cnt = 0
        while l <= r:
            c = (l+r)//2
            if c == key:
                return cnt
            elif c > key:
                r = c
                cnt += 1
            else:
                l = c
                cnt += 1

    if bS(P, Pa) < bS(P, Pb):
        result = 'A'
    elif bS(P, Pa) > bS(P, Pb):
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')