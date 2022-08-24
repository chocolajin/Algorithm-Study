# 세로 리스트 만들기
def turn_list(lst):
    new_list = ['' for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_list[i] += lst[j][i]
    return new_list
# 회문검사
def pal(lst):
    maxV = 0
    for i in range(len(lst)): # 리스트100줄을 처음부터 한 줄씩 뽑아낸다
        for j in range(len(lst),-1,-1): # 길이 j 짜리 회문
            for k in range(len(lst)-j+1):
                # 리스트의 i번째 줄의 문자열에서 k 번째 글자부터 길이 j인  t
                t = lst[i][k:k+j]
         
                # 회문검사
                for l in range(len(t)//2):
                    if t[l] != t[-l-1]:
                        break
                else:
                    if maxV < len(t):
                        maxV = len(t)
    return maxV


for tc in range(1,11):

    T = int(input())
    # case = [input() for _ in range(10)]
    case = [input() for _ in range(100)]

    if pal(case) >= pal(turn_list(case)):
        print(f'#{tc} {pal(case)}')

    elif pal(case) < pal(turn_list(case)):
        print(f'#{tc} {pal(turn_list(case))}')