for tc in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    
    cnt = 0
    for i in range(2, N-2):

        minH= 255
        for j in range(i-2,i+3):
            if i !=j:
                if minH > arr[i]-arr[j]:
                    minH = arr[i]-arr[j]
        if minH > 0:
            cnt += minH

    print(f'#{tc} {cnt}')