T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []

    for w in word:
        if stack:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)
    print(f'#{tc} {len(stack)}')