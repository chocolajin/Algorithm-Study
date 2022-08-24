T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = [int(x) for x in input()]

    cnt = [0] * 10

    for i in range(N):
        cnt[ai[i]] += 1

    result = 0
    maxN = 0
    for i in range(10):
        if cnt[i] >= result:
            result = cnt[i]
            maxN = i

    print(f'#{tc} {maxN} {result}')