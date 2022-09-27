# 퀵정렬
# (partition)
# 1.피벗잡고, 피벗을 기준으로 큰 값과 작은 값 구분하기
# 2. 피벗보다 작은값을 퀵 정렬, 피벗보다 큰 값 퀵 정렬
# 3. 단, 요소가 하나이면 멈춰

# 피벗기준 큰 값 작은 값으로 나눠주고, 피벗의 위치를 반환하는 함수
def partition(left, right):
    # 피벗잡고, 큰값, 작은값으로 구분하기
    pivot = arr[left]
    i, j = left, right
    while i <= j:
        # i 증가 시키면서 pivot보다 큰값 찾기
        while i <= j and arr[i] <= pivot:
            i += 1
        # j 감소 시키면서 pivot보다 작은값 찾기
        while i <= j and arr[j] > pivot:
            j -= 1
        # 위치교환
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j
#배열의 주어진 구간을 정렬하는 함수
def quick_sort(l,r):
    if l < r:
        #1. partition
        p_idx = partition(l, r)
        # 2. 피벗을 기준으로 작은 값과, 큰값을 다시 정렬
        #  피벗은 자기 위치를 찾은거니 정렬에 포함하지 않음
        quick_sort(l, p_idx-1)
        quick_sort(p_idx+1, r)

arr = [9,8,7,6,5,4,3,2,1]
N = len(arr)
quick_sort(0,N-1)
print(arr)
