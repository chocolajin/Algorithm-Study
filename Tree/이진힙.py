import sys
sys.stdin = open('input.txt', 'r')
# code1
def heap_push(value):
    global heap_count
    heap_count += 1
    heap[heap_count] = value

    current = heap_count
    parent = current // 2

    while parent and heap[current] < heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [None] * (N+1)
    heap_count = 0
    data = list(map(int, input().split()))
    for i in data:
        heap_push(i)
    cnt = 0
    a = N // 2
    while True:
        if a == 0:
            break
        cnt += heap[a]
        a = a // 2
    print(f'#{tc} {cnt}')

