T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    case = list(map(int, input().split()))

    for i in range(M):
        case.append(case.pop(0))
    print(f'#{tc} {case[0]}')