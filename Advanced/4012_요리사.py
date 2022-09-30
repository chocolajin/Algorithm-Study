import sys
sys.stdin = open('input.txt', 'r')

def com(n, r, s):  # n개에서 r개를 고르는 조합, s : 선택할 수 있는 구간의 시작
    global minV
    if r == 0:
        sumA = 0
        sumB = 0

        for i in range(N):
            for j in range(N):
                if i in comb and j in comb:
                    sumA += data[i][j]
                if i not in comb and j not in comb:
                    sumB += data[i][j]
        result = abs(sumA-sumB)
        if minV > result:
            minV = result

    else:
        for i in range(s, n-r+1):
            comb[r-1] = arr[i]
            com(n, r-1, i+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = [x for x in range(N)]
    minV = 0xffffffffffffffffffffff
    comb = [0] * (N//2)
    com(N, N//2, 0)
    print(f'#{tc} {minV}')
