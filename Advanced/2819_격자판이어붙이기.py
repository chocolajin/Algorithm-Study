def dfs(r, c, cnt, num):

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num += str(data[r][c])
    if cnt == 6:
        result.update([num])
        return
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, cnt+1, num)
T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,'')
    print("#{} {}".format(tc,len(result)))