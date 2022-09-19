import sys
sys.stdin = open('input.txt', 'r')

def inorder(v):
    global cnt
    if v > N:
        return
    inorder(v*2)
    tree[v] = cnt
    cnt += 1
    inorder(v*2 +1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
