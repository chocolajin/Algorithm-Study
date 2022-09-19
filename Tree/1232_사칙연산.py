#  v 계산하려고 하는 노드 번호
def postorder(v):
    # v번 노드가 가진 값이 연산자가 아닌경우에는 node의 value를 그대로 반환
    if data[v].isdigit():
        return float(data[v])
    # 왼쪽자식 결과 얻고
    # 오른쪽 자식 결과 얻어서
    # 연산해서 반환
    r1 = postorder(child[0][v])
    r2 = postorder(child[1][v])
    if data[v] == '+':
        return r1 + r2
    elif data[v] == '-':
        return r1 - r2
    elif data[v] == '*':
        return r1 * r2
    else:
        return r1 / r2

T = 10
for tc in range(1,T+1):
    N = int(input())
    # 각 노드의 자식 노드의 정보가 들어가는 배열
    child = [[0] * (N+1) for _ in range(2)]
    # 각 노드가 가지고 있는 value를 저장하는 배열
    data = [0] * (N+1)  
    for i in range(N):
        info = input().split() #노드 정보
        # input 이 4개일 수도 있고 2개일 수도 있음..
        if info[1].isdigit():
            data[int(info[0])] = info[1]
        else:   # 연산자일 경우는 왼쪽과 오른쪽 자식이 존재
            data[int(info[0])] = info[1]
            child[0][int(info[0])] = int(info[2])
            child[1][int(info[0])] = int(info[3])
    # 트리에 저장했으니.. 순회
    result = postorder(1)
    print(f'#{tc} {int(result)}')


#code2

def postorder(n):
    global stack
    if par[n]:
        postorder(ch1[n])
        postorder(ch2[n])

        if par[n].isdigit():
            stack.append(int(par[n]))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if par[n] == '*':
                stack.append(num1*num2)
            elif par[n] == '/':
                stack.append(num1//num2)
            elif par[n] == '+':
                stack.append(num1+num2)
            elif par[n] == '-':
                stack.append(num1-num2)

for tc in range(1, 11):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    par = [0] * (N + 1)
    arr = [list(input().split()) for _ in range(N)]
    for i in range(N):
        par[int(arr[i][0])] = arr[i][1]

        if len(arr[i]) == 4:
            p = int(arr[i][0])
            ch1[p] = int(arr[i][2])
            ch2[p] = int(arr[i][3])

    stack = []
    postorder(1)
    print(f'#{tc} {stack[0]}')





