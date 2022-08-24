def word(lst):
    sum_list = []
    for i in range(N):
        sumV = 0
        for j in range(N):
            if lst[i][j] == 1:
                sumV += 1
            else:
                sum_list += [sumV]
                sumV = 0
            if j == N-1 and sumV == K:
                sum_list += [sumV]
    cnt = 0
    for i in range(len(sum_list)):
        if sum_list[i] == K:
            cnt += 1
    return cnt

def turn_list(lst):
    new_list = [[]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_list[i] += [lst[j][i]]
    return new_list

T = int(input())
for tc in range(1, T + 1):
    N, K = (map(int, input().split()))
    case = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {word(case) + word(turn_list(case))}')