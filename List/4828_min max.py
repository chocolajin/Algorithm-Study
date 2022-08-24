T = int(input())

for tc in range(1, T+1):

    N = int(input())

    ai = list(map(int, input().split()))

    maxN = 0
    for i in ai:
        if maxN < i:
            maxN = i

    minN = 1000000
    for i in ai:
        if minN > i:
            minN = i

    result = maxN - minN
    print(f'#{tc} {result}')