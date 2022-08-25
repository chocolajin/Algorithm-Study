for tc in range(1,11):

    T = int(input())
    case = [list(map(int, input().split())) for _ in range(100)]
    # print(case)
    # 마지막 줄에서 2를 찾아라! 마지막줄 = for i in rangr(100) if case(99,i)==2 start=i
    # <1>올라가 <2>만약 좌나 우로 길이 있으면(1이면) 글로가 좌우 없으면 위로가 <3>반복
    # 꼭대기 row 0 되면 그때 col 갑ㅅ은?

    for i in range(100):
        if case[99][i] == 2:
            cpoint = i
            rpoint = 98

            while rpoint != 0:

                if 0 <= cpoint+1 < 100 and case[rpoint][cpoint+1] == 1:
                    while cpoint+1 < 100 and case[rpoint][cpoint+1] != 0:
                        cpoint += 1

                elif 0 <= cpoint-1 < 100 and case[rpoint][cpoint-1] == 1:
                    while cpoint-1 >= 0 and case[rpoint][cpoint-1] != 0:
                        cpoint += -1

                rpoint += -1

    print(f'#{tc} {cpoint}')


#code2 재귀
# r : 행, c :열 , d : 방향
def move(r,c,d):
    if r == 99:
        if ladder[r][c] == 2:
            return True
        else :
            return False
    if d == 0 :
        if 0 <= c - 1 < 100 and ladder[r][c - 1]:  # 왼쪽으로 갈 수 있음
            return move(r, c-1, 1)
        elif 0 <= c + 1 < 100 and ladder[r][c + 1]:
            return move(r, c + 1, 2)
        else:
            return move(r+dr[d], c, d)
    else:
        if 0 <= r + 1 < 100 and ladder[r + 1][c]:
            return move(r + 1, c, 0)
        else:
            return move(r, c+dc[d], d)
dr = [1, 0, 0]  # 방향 번호와 일치하도록 델타배열 선언
dc = [0, -1, 1]
for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):    #모든 열 탐색
        c = i
        if ladder[0][i]:
            result = move(0, i, 0)
            # print (result)
            if result:
                print(f'#{tc} {i}')
                break