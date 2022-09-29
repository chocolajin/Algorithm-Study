def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [x for x in range(0, N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    for j in range(1, N+1):
        parent[j] = find_set(j)
    result = len(set(parent))-1

    print(f'#{tc} {result}')