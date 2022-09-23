#code1
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    minV = sum(S)
    for i in range(1 << N):
        sumV = 0
        for j in range(N):
            if i & (1 << j):
                sumV += S[j]
        if sumV >= B and sumV < minV:
            minV = sumV
    print("#{} {}".format(tc,minV-B))