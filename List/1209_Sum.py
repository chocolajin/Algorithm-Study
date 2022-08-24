for tc in range(1,11):
    T = int(input())
    case = [list(map(int,input().split())) for _ in range(100)]
    maxcnt = 0
    cntdl = 0
    cntdr = 0
    for i in range(100):
        cntdl += case[i][i]
        cntdr += case[i][100-1-i]
        cntr = 0
        cntl = 0
        for j in range(100):
            cntr += case[i][j]
            cntl += case[j][i]      
        if cntdr > maxcnt :
            maxcnt = cntdr
        if cntdl > maxcnt : 
            maxcnt = cntdl
        if cntr > maxcnt :
            maxcnt = cntr
        if cntl > maxcnt : 
            maxcnt = cntl
    print(f'#{tc} {maxcnt}')