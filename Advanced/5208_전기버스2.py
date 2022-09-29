#code1

def dfs(idx, cnt, remain):
    global minV

    if minV <= cnt:
        return

    if idx == N:
        if minV > cnt:
            minV = cnt
            return

    dfs(idx+1, cnt+1, data[idx]-1)
    if remain > 0:
        dfs(idx+1, cnt, remain-1)

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    minV = 0xffffffff
    dfs(2, 0, data[1]-1)
    print("#{} {}".format(tc, minV))









#code2
T = int(input())
for tc in range(1, T + 1):
    N, *M_lst = map(int, input().split())
    position = 0
    idx = 0
    cnt = 0
    while position < N - 1:
        idx = position + M_lst[position]  # 현재위치에서 최대로 갈수있는 인덱스
        for i in range(position + 1, position + M_lst[position]):  # 최대로 갈수있는 범위내에서
            if M_lst[i] > M_lst[position + M_lst[position]] + 1:  # 최대인댁스보다 더멀리갈수 있는게 있다면
                idx = i
        position = idx
        idx = position + M_lst[position]  # 현재위치에서 최대로 갈수있는 인덱스
        cnt += 1

        if idx >= N - 1:
            break
    print(f'#{tc} {cnt}')