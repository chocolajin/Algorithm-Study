#code1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x : x[1])
    e = data[0][1]
    cnt = 1
    for i in range(1,N):
        if data[i][0] >= e:
            e = data[i][1]
            cnt += 1

    print(f'#{tc} {cnt}')



#code2
import sys
sys.stdin = open('input.txt', 'r')

def solve(i,j): # i번 화물차가 사용하고 나서 이후 도크를 사용한 화물차를 합집합으로 모으기(마지막 화물차(j)전에)
    m = i + 1    # i번 화물차 다음의 m번 화물차라고 가정
    while m < j and arr[m][0] < arr[i][1]:    # m번 화물차가 마지막 화물차전이면서, 현재 i번 화물차의 종료시간보다 m번 화물차의 시작시간이 빠르면
        m += 1    # 다음 화물차를 모색하자
    tmp = set()   # tmp라는 공집합을 두고,
    if m < j :    # m번 화물차가 여전히 마지막 화물차가 아니면,
        tmp.add(arr[m])      # m번째 화물차가 도크를 사용하는 경우
        tmp.update(solve(m,j))  # 또, m번째 화물차가 도크를 사용하고 나서 이후 도크를 사용한 화물차 더해주기
                                #  tmp에 solve(m, j): m번째 의 모든 요소를 추가(update)
        return tmp
    return tmp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [(0,0)]+[tuple(map(int, input().split())) for _ in range(N)]   # 화물차의 모음, 화물차의 개수와 arr 에서의 인덱스를 일치하게
    arr.sort(key=lambda x: x[1])              # 종료 시간이 빠른 순서로 활동을 정렬
    # print(solve(0, N+1))                       # 인덱스 1번의 화물차부터 마지막 화물차까지의 활동선택
    print(f'#{tc} {len(solve(0, N+1))}')