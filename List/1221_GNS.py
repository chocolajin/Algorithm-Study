#code1
lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(T):
    tc, N = input().split()
    case = input().split()
    arr = []
    for i in range(int(N)): # case 요소 하나씩 뽑아
        for j in range(len(lst)):
            if lst[j] == case[i]: # case의 요소가 lst의 요소와 같으면 lst의 인덱스가져옴
                arr.append(j) # 숫자로 만들어진 리스트 만들기
    # 버블정렬
    for i in range(int(N)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                case[j], case[j+1] = case[j+1], case[j]
    print(tc)
    print(' '.join(case))




#code2
def GNS_sort(arr):
    GNS_value = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # arr 정렬하기 : 버블정렬
    # 요소 2개 비교해서 큰값 뒤로 보내기
    # (큰 원소 뒤로 보내기 작업) * N 번 수행
    for j in range(N-1):
        #가장 앞쪽 원소부터 제일 뒤 원소까지 2개씩 비교해서 큰값 뒤로 보내기
        for i in range(N-1-j):
            if GNS_value[arr[i]] > GNS_value[arr[i+1]]:   #앞쪽 요소가 뒤쪽요소보다 더 크면 자리바꾸기
                arr[i], arr[i+1] = arr[i+1], arr[i]





#code3
def GNS_sort2(arr):
    GNS_value = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # 카운팅 정렬
    # 각 요소가 몇 번 나왔는지 숫자세기
    # 누적합구하기(요소 몇번째 자리에 들어가야 하는지 위치구하기)
    # 요소들을 위치보고 복사하면 됩니다..
    K = 10
    counts = [0]*K
    sorted_arr = [''] * N
    for i in range(N):
        index = GNS_value[arr[i]]
        counts[index] += 1
    for i in range(1,K):
        # counts[i] = counts[i] + counts[i-1]
        counts[i] += counts[i-1]
    #새로운 배열에 요소가 들어갈 위치에 값을 복사
    for i in range(N):
        # arr[i]요소가 들어갈 자리(counts[GNS_value[arr[i]]])에다가 넣어주기
        counts[GNS_value[arr[i]]] -= 1
        sorted_arr[counts[GNS_value[arr[i]]]] = arr[i]
    return sorted_arr

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    # GNS 숫자 배열 입력받기
    arr = input().split()
    #GNS_sort(arr)
    result = GNS_sort2(arr)
    print(f'{tc}')
    # print(*arr)
    print(*result)

