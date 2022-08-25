import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    T = int(input())
    case = [list(map(int, input().split())) for _ in range(100)]
    minV = 10000000
    cpointV = 0
    for i in range(100):
        if case[99][i] == 1:
            cpoint = i
            rpoint = 98
            cnt = 0
            while rpoint != 0:
                if 0 <= cpoint+1 < 100 and case[rpoint][cpoint+1] == 1:
                    while cpoint+1 < 100 and case[rpoint][cpoint+1] != 0:
                        cpoint += 1
                        cnt += 1
                elif 0 <= cpoint-1 < 100 and case[rpoint][cpoint-1] == 1:
                    while cpoint-1 >= 0 and case[rpoint][cpoint-1] != 0:
                        cpoint += -1
                        cnt += 1
                rpoint += -1
                cnt += 1
            if cnt < minV:
                minV = cnt
                cpointV = cpoint
    print(f'#{tc} {cpointV}')