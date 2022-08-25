#code1
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    charge_stop = [0]*(N+1)
    for i in charge:
        charge_stop[i] += 1
    cnt = 0
    start = 0
    while True:
        end = start + K
        if end >= N:
            break
        for j in range(end, start, -1):
            if charge_stop[j] == 1:
                cnt += 1
                start = j
                break
        else:
            cnt = 0
            break
    print(f'#{tc} {cnt}')




#code2
T = int(input())
for tc in range(1,T+1):
    K, N, M  = map(int,input().split())
    battery = list(map(int,input().split()))

    stations = [0]*N #인덱스에 해당하는 정류소에, 충전소가 있으면 1, 없으면 0
    for idx in battery:
        stations[idx] = 1
    #[0,1,0,1,0,0,1,0,0,1,0,0]

    cnt = 0     #충전 횟수 저장 변수
    position = 0 # 현재 위치
    # 가능한 멀리 가는 동작을 반복
    while True:
        #멀리있는 충전소 찾아서 이동하기
        # 내가 갈 수 있는 최대 위치 : position + K
        # position + K : 도착지점 이상이라면 이동할 필요가 없음
        position += K
        if position >= N:   #도착지에 도착함!
            break

        #가장 멀리있는 충전소 찾기
        for i in range(position,position-K,-1):
            if stations[i] == 1:   # 충전소가 있음
                cnt += 1
                position = i
                break   #충전소 찾기 중단
        else:   # break가 안걸렸다! >>> 충전소가 없음
            cnt = 0
            break  #다음칸으로 이동하는 반복 중단

    print(f'#{tc} {cnt}')



#code3
T = int(input())
for tc in range(1,T+1):
    K, N, M  = map(int,input().split())
    stations = list(map(int,input().split()))
    #일단 갈 수 있으면 지나쳐 가고, 갈 수 없으면,이전에 충전
    #양쪽 끝에 출발점과 도착점 추가
    stations.insert(0, 0)
    stations.append(N)
    position = 0
    cnt = 0
    for i in range(1,M+2):  #0번빼고, 2개 추가했으니 M+2
        #i-1번에서 i번으로 이동 불가할 때,
        if (stations[i] - stations[i-1]) > K:
            cnt = 0
            break
        #i-1번에서 i번으로 충전하면 올 수 있는 상황
        #그런데... 이 시점에 현재위치에서는 i번으로 못온다면?
        if stations[i] > position + K:
            position = stations[i-1]
            cnt += 1
        # else: # 도착가능...아무작업 안해도 됩니다.
    print(f'#{tc} {cnt}')

