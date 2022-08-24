T = int(input())
for tc in range(1, T+1):
    case = input()
    stack = []
    cnt = 0
    for i in range(len(case)):
        if case[i] == '(':
            stack.append(case[i])
        if case[i] == ')' and case[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        if case[i] == ')' and case[i-1] == ')':
            stack.pop()
            cnt += 1
    print(f'#{tc} {cnt}')