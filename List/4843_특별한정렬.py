T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = list(map(int, input().split()))

    for i in range(N):
        maxI = i
        minI = i
        for j in range(i+1, N):
            if i % 2 != 0:
                    if case[minI] > case[j]:
                        minI = j
            else:
                    if case[maxI] < case[j]:
                        maxI = j
        if i % 2 != 0:
            case[i], case[minI] = case[minI], case[i]
        else:
            case[i], case[maxI] = case[maxI], case[i]

    print(f'#{tc} {" ".join(map(str, case[0:10]))}')