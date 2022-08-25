#code1
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

#code2
for tc in range(1, 11):
    #문제풀거고
    N = int(input())
    buildings = list(map(int, input().split()))
    #문제 풀면되는데....
    # 2~N-3번 건물까지 조망권 확보된 세대 계산하기
    result = 0
    for i in range(2, N-2):
        #조망권 확보된 세대 계산하기
        #양쪽 2칸에 있는 건물들 높이 확인하기
        # 제일 높은 건물 높이 찾고, 현재 건물이 주변 건물보다 높이가
        # 높으면 조망권이 확보 되었으니 더해주기
        # i-2번 건물부터 i+2 번 건물까지 제일 높은 건물 높이 구하기
        # 최대값 찾을 때는 , 최대값 저장하는 변수의 초기값은 최대한 작게
        # 최소값을 찾을땐, 변수의 초기값을 최대한 크게
        max_height = 0
        for j in range(i-2, i+3):
            if j == i:
                continue
            if buildings[j] > max_height:
                max_height = buildings[j]

        # for b in [buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]]:
        #     if b > max_height:
        #         max_height = buildings[j]

        if max_height < buildings[i]:   # 조망권이 확보된 세대가 있음
            # 확보된 세대수를 결과에 더해주기
            result += (buildings[i] - max_height)

    print(f'#{tc} {result}')
