def div(begin,end):
    if begin == end:
        return begin
    a = div(begin,(begin+end)//2)
    b = div((begin+end)//2 + 1, end)
    return winner(a,b)
def winner(a,b):
    if case[a] == case[b]:
        return a
    elif case[a]-case[b] == 1 or case[a]-case[b] == -2:
        return a
    return b

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = list(map(int, input().split()))
    x = div(0, N - 1)
    print(f'#{tc} {div(0,N-1)+1}')
