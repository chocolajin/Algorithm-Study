#code1
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



#code2
dr = [0,1,0,-1]
dc = [1,0,-1,0]
# 0 번 오른쪽, 1번 아래쪽, 2번 왼쪽 3번 위쪽
d = 0   #  달팽이가 움직일 방향을 정하는 변수
num = 1 # 달팽이가 지나간 위치에 적어줄 숫자
N = 5
arr = [[0] * N for _ in range(N)]
r, c = 0, 0 #시작점, 현재위치
while num <= N*N:
    # 달팽이 움직이기
    # 근데, 만약에 움직이려는 칸으로 못가면, 방향전환해주기
    print((r, c),num)
    arr[r][c] = num
    num += 1
    #다음칸으로 이동, 내가 이동중인 방향으로 계속이동
    # r= r + dr[d]
    r += dr[d]
    c += dc[d]
    if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] != 0:  #범위 비정상
        r -= dr[d]
        c -= dc[d]
        #방향전환
        d = (d + 1) % 4
        r += dr[d]
        c += dc[d]

for row in arr:
    print(*row)
