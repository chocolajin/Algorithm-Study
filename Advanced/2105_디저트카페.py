#code1
# r,c: 현위치, dir: 움직이는 방향, visited: 방문기록
def dfs(r,c,dir,visited):
    global maxV

    #한바퀴 돌아서 다시 돌아온 경우를 검사하기 위해 vidited검사
    if visited and (r,c) == (i,j):
        if maxV < len(visited):
            maxV =len(visited)
        return
    if r < 0 or r>=N or c<0 or c>=N or data[r][c] in visited:
        return

    visited.add(data[r][c])

    #직진
    dfs(r+dr[dir],c+dc[dir],dir,visited)
    #방향전환
    if dir < 3:
        dfs(r+dr[dir+1],c+dc[dir+1],dir+1,visited)
    visited.remove(data[r][c])

dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1

    for i in range(N):
        for j in range(N):
            dfs(i,j,0,set())

    print("#{} {}".format(tc,maxV))