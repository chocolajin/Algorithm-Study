T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pas = [[0]*i for i in range(1,N+1)]
    for i in range(N):
        for j in range(i+1):
            if j == 0:
                pas[i][j] = 1
            elif j == i:
                pas[i][j] = 1
            else:
                pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
    print(f'#{tc}')
    for i in range(len(pas)):
        for j in range(len(pas[i])):
            print(pas[i][j],end=' ')
        print()


#code2
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 1 0 0 0
    # 1 1 0 0
    # 1 2 1 0
    # 1 3 3 1
    arr = [[1]+[0] * (N-1) for _ in range(N)]
    for i in range(1, N):  #모든 행에 대해서 수행
        for j in range(1, i+1):
            # i-1행의 j열과  j-1 열의 값 더해서
            # 내자리에 넣어주기
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j],end=' ')
        print()
