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
