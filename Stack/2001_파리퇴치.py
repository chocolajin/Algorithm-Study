T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    case = [list(map(int, input().split())) for i in range(N)]
    # print(case)
    maxV = 0
    idx = 0
    for k in range(N-M+1):
        for l in range(N-M+1):
            sumV = 0
            for i in range(M):
                for j in range(M):
                    a = case[k][l]
                    sumV += case[k + i][l+ j]
            if sumV > maxV:
                maxV = sumV

    print(f'#{tc} {maxV}')

#code2
T = int(input())
for tc in range(1, T+1):
    # N은 배열크기 M은 파리채 크기
    N, M = map(int, input().split())
    case = [list(map(int, input().split())) for i in range(N)]

    maxV = 0 # sumV 값 중 가장 큰 값
    # 배열크기 - 파리채 크기
    for k in range(N-M+1):
        for l in range(N-M+1):
            sumV = 0 # 잡은 파리 수 합
            for i in range(M):
                for j in range(M):
                    sumV += case[k + i][l+ j]
            # sumV가 현재의 maxV보다 크면 바꿔줌
            if sumV > maxV:
                maxV = sumV

    print(f'#{tc} {maxV}')
