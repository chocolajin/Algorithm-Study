T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    queue = []
    cnt = 1
    while Ci:
        if len(queue)==N:
            while True:

                cheese, num = queue.pop(0)
                if cheese//2 != 0:
                    queue.append((cheese//2 , num))
                else:
                    break
        else:
            queue.append((Ci.pop(0),cnt))
            cnt += 1



    while True:
        if len(queue) == 1 :
            print(f'#{tc} {queue[0][1]}')
            break
        else:
            cheese, num = queue.pop(0)
            if cheese//2 != 0:
                queue.append((cheese//2 , num))



#code2
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    oven = []               # 오븐에 들어가 있는 피자
    pizza = []              # 대기 중인 피자

    for i in range(N):
        oven.append([i, arr[i]])    # i = 피자를 구별하기 위한 표시. 0번 피자부터. arr[i] = 치즈 양
    for i in range(N, M):
        pizza.append([i, arr[i]])

    while len(oven) != 1:
        num = oven.pop(0)
        if num[1] == 0:             # num[0] = 피자를 구별하기 위한 i가 입력되어 있고, num[1] = 치즈의 양
            if len(pizza) != 0:     # 현재 치즈의 양이 0이고 대기 중인 피자가 있으면 새로 추가. 없으면 넘어 감.
                pizza_num = pizza.pop(0)
                pizza_num[1] = pizza_num[1] // 2    # 맨 마지막에 append할 예정.
                oven.append(pizza_num)              # 차례가 오면 이미 한 바퀴 돌았으니 치즈 양을 미리 반으로 나눠서 추가.

        else:
            num[1] = num[1] // 2    # 현재 치즈의 양이 0을 초과하면 반으로 나눈 후 맨 뒤로 append.
            oven.append(num)
    result = oven[0][0] + 1         # 피자 번호가 0번 부터 시작했으니 + 1.
    print(f'#{tc} {result}')




#code3
test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        arr[i] = [arr[i], i]
    hot = [arr[0], arr[1]]
    pizza = 2
    while len(hot) > 1:
        while len(hot) < n and pizza < m:
            hot.append(arr[pizza])
            pizza += 1
        a, i = hot.pop(0)
        a //= 2
        if a != 0:
            hot.append([a, i])
    print(f'#{t} {hot[0][1]+1}')