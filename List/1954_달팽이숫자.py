T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = [[0]*N for _ in range(N)]
  
    go = N
    row = 0
    col = -1
    n = 1

    while True:
        #우로 가기
        for i in range(go):
            col += 1
            lst[row][col] = n
            n += 1
        
        go -= 1
        if go == 0:
            break

        #밑으로 가기
        for i in range(go):
            row += 1
            lst[row][col] = n
            n += 1

        #좌로 가기
        for i in range(go):
            col -= 1
            lst[row][col] = n
            n += 1
        
        go -= 1
        if go == 0:
            break

        #위로가기
        for i in range(go):
            row -= 1
            lst[row][col] = n
            n += 1
    print(f'#{tc}')
    for i in lst:
        for j in i:
            print(j,end=' ')
        print()
