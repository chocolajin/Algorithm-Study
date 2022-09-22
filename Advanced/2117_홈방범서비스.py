#code1
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 도시의크기, 집이 지불할수있는비용
    city = [list(map(int, input().split())) for _ in range(N)]
    home_list = []
    for i in range(N):
        for j in range(N):
            if city[i][j]:
                home_list.append((i, j))
    home_max = 0
    for k in range(1, N + 2):  # k의크기 : 모든 영역 다 채웠을 때 최대 n+1
        minus = k * k + (k - 1) * (k - 1)
        for i in range(N):
            for j in range(N):
                home = 0
                for h in home_list:  # 집의 좌표
                    x, y = h
                    if abs(i - x) + abs(j - y) < k:  # k영역안에있는지
                        home += 1
                if home * M - minus >= 0 and home_max < home:  # 손해가 없고, 최대값 찾기
                    home_max = home
    print(f'#{tc} {home_max}')






#code2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    city_data = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for k in range(N+1):
        for i in range(N):
            for j in range(N):
                cnt = 0
                for l in range(-k, k + 1):
                    for m in range(-k, k + 1):
                        if abs(l) + abs(m) <= k:
                            if 0 <= i + l < N and 0 <= j + m < N:
                                if city_data[i + l][j + m] == 1:
                                    cnt += 1

                if cnt * M >= k * k + (k + 1) * (k + 1):
                    if cnt > max_cnt:
                        max_cnt = cnt
    print(f'#{tc} {max_cnt}')