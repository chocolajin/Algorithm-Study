# 재귀는 같은 모양을 반복호출 >> 반복문 처럼 보일 수 있지만
# 특정한 함수 내부에서 똑같이 생긴 함수를 호출하는 것
def powerset(idx,status):
    if idx == N:
        #return : 함수 종료
        print(status)
        return None
    for i in range(2):
        status[idx] = i
        powerset(idx+1, status)
    #함수 마지막 줄에는 항상 return이 숨어 있음!
    #return : return None
    return None

N = 3
status = [0] * N
powerset(0, status)
