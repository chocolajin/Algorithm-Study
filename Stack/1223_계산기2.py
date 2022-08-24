for tc in range(1,11):
    N = int(input())
    case = input()
    stack = [] 
    arr = [] #후위 표기식 넣을 리스트
    #후위 표기식으로 바꾸기 
    for i in range(N):
        if case[i] == '*': # '*' 가 우선순위가 가장 높으므로 스택에 넣어준다.
            stack.append(case[i])
        elif case[i] == '+': # '+'가 우선순위가 가장 낮으므로 스택에서 pop한 후, 토큰의 연산자를 push한다.
            while stack:
                arr.append(stack.pop())
            stack.append(case[i])
        else: # 숫자가 나오면 arr에 넣어준다.
            arr.append(int(case[i]))
    while stack: # 스택에 남아있는 연산자를 모두 pop하고 arr에 너어준다. 
        arr.append(stack.pop())

    #연산하기
    for i in range(len(arr)): # arr에서 하나씩 뽑기
        if arr[i] != '*' and arr[i] != '+': # 숫자면 stack에 넣기
           stack.append(arr[i])
        else: # 연산자 나오면 피연산자 pop하고 연산자에 맞는 연산하고 스택에 넣기
            v1 = stack.pop()
            v2 = stack.pop()
            if arr[i] == '+':
                stack.append(v1+v2)
            else:
                stack.append(v1*v2)
    

    print(f'#{tc} {stack[0]}')