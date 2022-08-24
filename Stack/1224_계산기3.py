for tc in range(1, 11):
    N = int(input())
    case = input()

    pri = {'*':3, '/':3, '+':2, '-':2, '(':1}
    stack = []
    arr = []  # 후위 표기식 넣을 리스트
    # 후위 표기식으로 바꾸기
    for i in range(N):
        if case[i] == '(': # 여는 괄호는 스택에 넣기
            stack.append(case[i])
        elif case[i] in '*/+-': # 연산자일 때
            if stack: #스택이 비지 않았을 때
                if pri[case[i]] <= pri[stack[-1]]: # 스택 top이 더 우선순위가 높으면
                    while stack and pri[case[i]] <= pri[stack[-1]]: #스택 top의 우선순위가 낮을때 까지 pop하고 표기식에 넣기
                        arr.append(stack.pop())
                    stack.append(case[i]) # 다빼고 스택에 들어가기
                else: # 스택 top보다 우선순위가 높으면 그냥 스택에 넣기
                    stack.append(case[i])
            else: #스택이 비었으면 스택에 넣기
                stack.append(case[i])
        elif case[i] == ')': #닫는 괄호는 여는 괄호 나올 때 까지 팝하고 표기식에 넣은 후, 스택에 넣기
            while stack[-1] != '(':
                arr.append(stack.pop())
            stack.pop()
        else:  # 숫자가 나오면 표기식에 넣어준다.
            arr.append(case[i])
    while stack:  # 스택에 남아있는 연산자를 모두 pop하고 표기식에 넣어준다.
        arr.append(stack.pop())

    #연산하기
    for i in range(len(arr)):
        if arr[i] in '*/+-':
            num2 = stack.pop()
            num1 = stack.pop()
            if arr[i] == '*':
                stack.append(num1*num2)
            elif arr[i] == '/':
                stack.append(num1//num2)
            elif arr[i] == '+':
                stack.append(num1+num2)
            elif arr[i] == '-':
                stack.append(num1-num2)
        else:
            stack.append(int(arr[i]))
            

    print(f'#{tc} {stack.pop()}')