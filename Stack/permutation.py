# idx 번째 index 에다가 넣을 수 있는 숫자를 다 넣어보기
def permutation(idx):
    if idx == N:
        print(perm)
        return
    for i in range(N):
        if check[i] == 0:
            perm[idx] = arr[i]
            check[i] = 1
            permutation(idx + 1)    # idx 번째 숫자 결정했으니 다음 인덱스 결정
            check[i] = 0

def permutation2(idx):
    if idx == N:
        print(arr)
        return
    # idx 번째 요소랑 내 뒤에 있는 애랑 자리 바꾸기
    # 자리 안바꾸는거 포함
    for i in range(idx,N):
        arr[idx], arr[i] = arr[i], arr[idx]
        permutation2(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]








arr = [1,2,3]
#
N = len(arr)
perm = [0]*N
check = [0] * N # 순열만들때 사용한 idx를 표시하는 배열
# permutation(0)
permutation2(0)