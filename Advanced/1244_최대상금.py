#code1
def price(cnt, change):
    global maxV
    if cnt == change:
        result = int(''.join(N))
        if maxV < result:
            maxV = result
    else:
        for i in range(len(N) - 1):
            for j in range(i + 1, len(N)):
                N[i], N[j] = N[j], N[i]
                result = int(''.join(N))
                if result not in visit[cnt]:
                    visit[cnt].append(result)
                    price(cnt + 1, change)
                N[i], N[j] = N[j], N[i]

T = int(input())
for tc in range(1, T + 1):
    N, change = map(int, input().split())
    N = list(str(N))
    maxV = 0
    visit = [[] for _ in range(10)]
    price(0, change)
    print(f'#{tc} {maxV}')






#code2
# cnt번째 각 요소간 교환을 수행하는 함수
# cnt : 교환을 수행한 횟수
def solve(cnt):
    global max_value, count
    # 시간 줄이기 중복체크
    # 이미 한 번 교환 해본 카드들은 교환하지 않음
    # 단, 카드 모양과 교환 횟수까지 일치해야 한다.
    # count += 1
    num = int(''.join(data))
    if (cnt, num) in check:  # 이미 교환해본 케이스
        # 교환하지 않기
        return
    check.add((cnt, num))
    if cnt == N:    # 교환이 완료된 상태
        #교환이 완료가 된 상태에서 결과 확인하기
        # print(data)
        if num > max_value:
            max_value = num
        return
    #교환
    #교환 수행후, 재귀적으로 cnt+1 번째 교환을 수행한다.
    # 모든 요소에 대해서 요소 보다 뒤에 있는 요소와 교환하기
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            #교환
            data[i], data[j] = data[j], data[i]
            solve(cnt+1)
            #원래 모양으로 돌려놓기
            data[i], data[j] = data[j], data[i]

# 모든 카드 교환 경우의 수를 다 수행해보기
# 카드 교환 횟수 만큼
# 최종 교환을 완료했을 때, 만들어지는 경우의 수중, 가장 큰 수를 찾으면 됨
T = int(input())
for tc in range(1,T+1):
    data, N = input().split()
    # 계산을 위해서.. 문자열 리스트로 저장
    data = list(data)
    N = int(N)
    max_value = 0
    # count = 0
    check = set()
    solve(0)
    # print(count)
    print(f'#{tc} {max_value}')
