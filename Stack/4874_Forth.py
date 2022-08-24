def cal(expr):
    # 하나씩 읽으면서 피연산자이면 스택에 넣고
    # 연산자이면 스택에서 피연산자 두개 꺼냄
    # 다시 스택에 넣기
    stack = []
    for i in range(N):
        try :
            if expr[i] == '.':
                if len(stack) == 1:
                    return stack.pop()
                else:
                    return 'error'

            elif expr[i] in '*/+-':
                num2 = stack.pop()
                num1 = stack.pop()
                if expr[i] == '*':
                    stack.append(num1*num2)
                elif expr[i] == '/':
                    stack.append(num1//num2)
                elif expr[i] == '+':
                    stack.append(num1+num2)
                elif expr[i] == '-':
                    stack.append(num1-num2)
            else:
                stack.append(int(expr[i]))
        except:
            return 'error'

T = int(input())
for tc in range(1, T+1):
    case = list(input().split())
    N = len(case)
    print(f'#{tc} {cal(case)}')
