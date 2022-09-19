# 연산은 두가지
# 최대 높이 3인 트리를 이용해서 heap구현
# 최대힙
heap = [None]*16
# 맨 마지막 변수를 가리키는 변수
heap_count = 0

def heap_push(value):
    global heap_count
    # 1. 마지막 위치에 밸류넣기
    heap_count += 1
    heap[heap_count] = value
    # 2. 부모노드랑 비교해서 자식노드가 부모보다 더 크면 바꿔주기 반복

    current = heap_count
    parent = current // 2
    # 현재 노드가 루트가 아니고 자식 노드가 부모보다 더 크면 바꿈
    while current > 1 and heap[current] > heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2

def heap_pop():
    global heap_count
    # 1. 루트 반환
    result = heap[1]
    # 2. 마지막 요소를 루트 위치에 복사하기
    heap[1] = heap[heap_count]
    heap[heap_count] = None
    heap_count -= 1
    # 3. 부모노드랑 비교해서 자식노드가 부모보다 더 크면 바꿔주기 반복
    parent = 1
    child = parent*2
    if child+1 <= heap_count:
        if heap[child] < heap[child+1]:
            child += 1
    while child <= heap_count and heap[parent] < heap[child]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent*2
        if child + 1 <= heap_count:
            if heap[child] < heap[child + 1]:
                child += 1

    return result

heap_push(2)
heap_push(4)
heap_push(1)
heap_push(6)
heap_push(7)
heap_push(5)
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
