#code1

def partition(left,right):
    p = arr[left]
    i, j = left, right
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] > p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(l, r):
    if l < r:
        p_idx = partition(l,r)
        quick_sort(l, p_idx-1)
        quick_sort(p_idx+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0,N-1)
    print("#{} {}".format(tc, arr[N//2]))









#code2

# pivot 위치 구하는 함수 만들기
def partition(left, right):
    p = lst[left]
    i, j = left, right
    # i가 j보다 커지기 전까지 반복할건데!
    while i <= j:
        # i는 계속 증가시키면서 p보다 큰값 찾아주기(lst[i]가 p보다 작은동안 반복)
        while i <= j and lst[i] <= p:
            i += 1
        # j는 계속 감소시키면서 p보다 작은값 찾아주기(lst[i]가 p보다 큰동안 반복)
        while i <= j and lst[j] >= p:
            j -= 1
        # 만약에 i랑 j 비교해서 j가 더 크면 lst[i]랑 lst[j] 자리 바꿔주기
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    # while문 다 돌고나면 j < i가 됨(피봇과 lst[j] 자리 바꿔주기 -> j가 피봇 위치가 됨)
    lst[left], lst[j] = lst[j], lst[left]
    return j

# 퀵정렬 함수
def quick_sort(l, r):
    # l이 r보다 작으면
    if l < r:
        # 피봇 위치 s 구해주고, 피봇의 왼쪽 구간에서 퀵정렬, 오른쪽 구간에서 퀵정렬
        s = partition(l, r)
        quick_sort(l, s-1)
        quick_sort(s+1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(0, N-1)
    result = lst[N//2]
    print(f'#{tc} {result}')