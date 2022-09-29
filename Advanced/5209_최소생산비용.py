#code1

def solve(idx, sumV):
    global minV
    if sumV > minV:
        return
    if idx == N:
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            solve(idx + 1, sumV + data[idx][i])
            check[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    minV = 10000
    check = [0] * N
    solve(0, 0)
    print("#{} {}".format(tc, minV))









#code2

#### 1. 데이터 받기 #########################################################
############ 2. 함수 설정 ##################################################
################# 3. 함수 실행 및 정답 출력 ###################################

# --<<2. 비용의 최솟값 찾기 위한 함수>>-----------------------------    ------------------------------------------------------

def allocate_the_factory(idx, total_cost):
    # idx : 행,
    # total_cost : 지금까지 비용의 합

    global min_cost

    # --<<2-3. 과정 중 검증, 쓸데 없이 힘 빼지 말기>>-----------------------------------------------------------------------
    if total_cost > min_cost:
        return

    # --<<2-1. 종료 조건, 최솟값 검증>>----------------------------------------------------------------------------------
    if idx == N:                                    # 종료 조건
        if total_cost < min_cost:
            min_cost = total_cost

    # --<<2-2. 경로에 대한 합 구하기 위한 과정>>----------------------------------------------------------------------------
    for i in range(N):                              # 방문하지 않은 공장(열) 찾아가며 행을 순회할 예정
        if visited_fac[i] == 0:                     # 만약 방문하지 않은 공장이라면
            visited_fac[i] = 1                      # 방문표시 후(생산 배정한 후)

            # 배정한 공장의 비용을 total_cost에 더해준 채로 함수 재귀
            allocate_the_factory(idx + 1, total_cost + cost[i][idx])

            visited_fac[i] = 0                      # 다음 케이스 위해 방문 표시 해제


# --<<1. 데이터 받기>>----------------------------------------------------------------------------
T = int(input())                                    # 테스트 케이스 수 T 받기
for tc in range(1, T+1):                            # 테스트 케이스의 수 T 만큼 반복한다.
    N = int(input())                                # 공장 수이자 제품 수인 N 받기
    cost = [list(map(int, input().split())) for _ in range(N)]  # 데이터 입력받기

    visited_fac = [0] * N                           # 배정된 공장 표시 위한 리스트
    min_cost = 99 * (N**2) + 1                      # 생산비용의 최댓값 99

# --<<3. 함수 실행 및 정답 출력>>----------------------------------------------------------------------------
    # 인덱스 0,0 부터 합은 0인 상태로 함수 실행
    allocate_the_factory(0, 0)

    print(f'#{tc} {min_cost}')                      # 정답 출력