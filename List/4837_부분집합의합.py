T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(arr)
    cntV = 0
    for i in range(1 << n):
        sumV = 0
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                sumV += arr[j]
                cnt += 1
        if sumV == K and cnt == N:
            cntV += 1
    print(f'#{tc} {cntV}')