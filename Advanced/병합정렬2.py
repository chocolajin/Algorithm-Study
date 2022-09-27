# l,r : 정렬 대상 인덱스
def merge_sort(l,r):
    if l == r:
        return
    m = (l+r)//2
    merge_sort(l,m)
    merge_sort(m+1,r)
    merge(l,r)

def merge(l, r):
    merged_lst = []
    m = (l + r) // 2
    i = l
    j = m + 1
    # i와 j가 가리키는 요소값 비교해서 작은 순서대로 복사
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            merged_lst.append(arr[i])
            i += 1
        else:
            merged_lst.append(arr[j])
            j += 1
    # 작은 것들 비교해서 복사하고 난뒤에 남은 요소들 복사하기
    if i <= m: #왼쪽요소가 남은 경우
        for a in range(i,m+1):
            merged_lst.append(arr[a])
    if j <= r: # 오른쪽 요소가 남은경우
        for a in range(j,r+1):
            merged_lst.append(arr[a])
    # arr에 merged_lst 요소 복사하기
    idx = 0
    for a in range(l,r+1):
        arr[a] = merged_lst[idx]
        idx += 1

arr = list(map(int,input().split()))
N = len(arr)
merge_sort(0,N-1)
print(arr)