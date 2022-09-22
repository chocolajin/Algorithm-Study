#code1
T = int(input())

def solve(r,cnt,sumV):
    global minV
    if minV < sumV:
        return
    if cnt == N-1:
        if minV > sumV + data[r][0]:
            minV = sumV + data[r][0]
        return
    for i in range(1,N):
        if r != i and not visit[i]:
            visit[i] = 1
            solve(i, cnt+1,sumV + data[r][i])
            visit[i] = 0

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    minV = 1000000000

    solve(0,0,0)
    print(f'#{tc} {minV}')




#code2
import sys

sys.stdin = open('input.txt', 'r')


def sol(i, k):
    global minV
    if i == k:  # 자리 바꾸기 끝나면 1.옳은 경로를 고르고 2.비용 계산하기
        # print(p)                    # 2. 자리바꾸기로 만들어지는 경우
        sumV = 0
        for i in range(1, k):
            if p[0] == p[i]:
                f = p[:i + 1]  # 위의 경우에서 처음과 끝이 1이 되도록 잘라주기
                if len(f) == k:  # 잘랐을 때 길이가 N+1이면 옳은 경로
                    for i in range(k - 1):  # 비용 계산
                        sumV += arr[p[i]][p[i + 1]]
                    if sumV < minV:  # 비교를 통해 최소 비용을 확정하기
                        minV = sumV
    else:  # 자리를 바꾸는 과정
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            sol(i + 1, k)
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 비용에 대한 데이터 입력받기

    p = [0] + [x for x in range(N)]  # 1. 자리바꿈할 N+1 개의 숫자
    # print(p, len(p))
    minV = 100 * (N * N)  # 비용은 N*N개의 100이하 음이아닌 정수
    sol(1, N + 1)  # 0번째는 0으로 두고 1번째 자리부터 자리바꾸기
    print(f'#{tc} {minV}')  # 마지막

'''
    예를 들어, 

    N = 4
        0  1  2  3
      0 0 83 65 97
      1 82 0 78 6
      2 19 19 0 82
      3 6 34 94 0

    + 사무실(1)에서 출발해 각 구역을 한 번씩만 방문하고 사무실(1)로 돌아오기 때문에 path 는
        1, 2, 3, 4, 1의 5개의 숫자를 하나씩 사용해 나열하는 경우의 비용을 계산하기:

     + 일반적으로, 
     사무실(1)에서 출발해 각 구역을 한 번씩만 방문하고 사무실(1)로 돌아오기 때문에 path 는
        1, 2, 3, ..., N,1의 (N+1)개의 숫자를 하나씩 사용해 나열하는 경우로 path를 결정하고 옳은 path의 비용을 계산하기

     1 - 1 ) path를 고르자

    # 1, 2, 3, ..., N,1의 (N+1)개의 숫자를 하나씩 사용해 나열하는 모든 경우에 대해서
    # 배열의 길이를 1에서 시작해 1로 끝나게 길이를 잘라 그 길이가 N + 1이면 옳은 path로 간주

    # 1 + 123 :   1123 -> 11      (X)
    # 1 + 132 :   1132 -> 11      (X)
    # 1 + 213 :   1213 -> 121     (X)
    # 1 + 231 :   1231 -> 1231    (O)     - path 1
    # 1 + 321 :   1321 -> 1321    (O)     - path 2
    # 1 + 312 :   1312 -> 131     (X)


    1 - 2 ) 비용을 계산하자 
    그런데
    path1에 대해,
            1231의 비용:
                문제에선, e[1][2] + e[2][3] + e[3][1], arr[0][1] + arr[1][2]+ arr[2][0]이므로 
                경로 1을 0121로 간주
    path2에 대해, 
            1321의 비용:
                ...
                경로 2를 0210로 간주

    따라서 자리바꿈을 할 수 있는 0, 0, 1, ...N-2 임에 유의해 자리바꿈원본의 리스트 p를 설정

    '''