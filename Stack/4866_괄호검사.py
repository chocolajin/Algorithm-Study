T = int(input())
for tc in range(1, T+1):
    code = input()

    stack = []
    result = 1
    for c in code:
        if c == '(' or c == '{':
            stack.append(c)
        if c == ')' or c == '}':
            if not stack:
                result = 0
                break
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ')' and stack[-1] == '{':
                result = 0
                break
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == '}' and stack[-1] == '(':
                result = 0
                break
    else:
        if len(stack) == 0:
            result = 1
        else:
            result = 0

    print(f'#{tc} {result}')