#code1

def b_search(n, lst, key):
    l = 0  # 탐색 구간의 시작 인덱스
    r = n - 1  # 탐색 구간의 끝 인덱스
    move_d = ''  # 탐색 방향
    while l <= r:
        m = (l + r) // 2  # 중심원소 인덱스
        if lst[m] == key:  # 찾았다!
            return 1

        elif lst[m] > key:  # 찾으려는 key가 중간보다 작다
            r = m - 1  # => 왼쪽가서 찾자

            # 처음이거나 직전에 반대방향(오른쪽)으로 갔었다면
            if move_d == '' or move_d == 'right':
                move_d = 'left'  # 탐색방향 left 로 바꿔줌

            else:  # 직전에 왼쪽이었는데 또 왼쪽이면 실패!
                break
        else:  # 찾으려는 key가 중간보다 크다
            l = m + 1  # => 오른쪽가서 찾자

            # 처음이거나 직전에 반대방향(왼쪽)으로 갔었다면
            if move_d == '' or move_d == 'left':
                move_d = 'right'  # 탐색방향 right 로 바꿔줌

            else:  # 직전에 오른쪽이었는데 또 오른쪽이면 실패!
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for num in B:
        result = b_search(N, A, num)
        cnt += result

    print("#{} {}".format(tc, cnt))
