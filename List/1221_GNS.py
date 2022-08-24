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