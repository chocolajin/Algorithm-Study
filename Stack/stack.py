# 스택구현해서 값 넣어보기
# class 로 구현해보기
class Stack:
    # 속성 : 실제 데이터를 저장할 배열(리스트) - 고정길이,
    #        마지막원소를 가리키는 변수(stack pointer) : top
    # 기능 : push, pop, peek, size, is_empty
    def __init__(self, length):
        self.stack = [None]*length
        self.top = -1
    
    # 요소를 stack 마지막에 저장하고, 만약에 가득차서 못넣을경우 'overflow' 출력
    def push(self,val):
        if self.is_full():
            print('overflow')
        else:
            self.top += 1
            self.stack[self.top] = val

    # 마지막 요소를 삭제하고, 반환, 요소가 없는경우 'underflow'
    def pop(self):

        if self.is_empty():
            print('underflow')
            return None
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    # 마지막 요소를 반환, 요소가 없는경우 'underflow'
    def peek(self):
        if self.is_empty():
            print('underflow')
            return None
        return self.stack[self.top]

    # 현재 요소의 개수 반환,
    def size(self):
        return self.top + 1

    # 요소가 없으면, True, 있으면 False 반환
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    #가득 찼으면, True, 아니면 False 반환
    def is_full(self):
        if self.top == len(self.stack)-1:
            return True
        return False

my_stack = Stack(10)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.peek(), my_stack.size(), my_stack.is_full(), my_stack.is_empty())

