#원형큐
# 데이터가 저장될 배열,
# front,rear 필요
# 기능 : enQueue, deQueue, peek,is_empty, is_full, queue_print
class Queue:
    def __init__(self,N):
        self.queue = [None]*N
        self.front = 0
        self.rear = 0
    def enQueue(self,data):
        #rear 뒤쪽에 요소 넣기
        if not self.is_full():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data
        else:
            raise IndexError
    def deQueue(self):
        #front에 있는 요소 삭제 및 반환
        if not self.is_empty():
            self.front = (self.front+1) % len(self.queue)
            return self.queue[self.front]
        return None

    def peek(self): # 가장 앞쪽에 있는 요소를 반환
        # front 바로 뒤에 있는 요소
        if not self.is_empty():
            return self.queue[(self.front+1) % len(self.queue)]
        return None
    
    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear+1) % len(self.queue) == self.front

    def queue_print(self):
        # front + 1 ~ rear 출력하기
        idx = self.front
        while idx != self.rear:
            idx = (idx + 1) % len(self.queue)
            print(self.queue[idx], end=' ')
        print()


T = 10
for _ in range(T):
    tc = input()
    data = list(map(int,input().split()))
    queue = Queue(9)
    for d in data:
        queue.enQueue(d)

    cnt = 0
    while True:
        # 제일 앞요소 빼서, cnt 빼고, 뒤에 넣기
        num = queue.deQueue()
        num = num - (cnt) % 5 - 1
        if num < 0:
            num = 0
        queue.enQueue(num)
        cnt += 1
        if num == 0:
            break

    print(f'#{tc}',end=' ')
    queue.queue_print()





