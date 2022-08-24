def turn_list(lst):
    new_list = ['' for _ in range(8)]
    for i in range(8):
        for j in range(8):
            new_list[i] += lst[j][i]
    return new_list

def pal(lst,N):
    cnt = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])-N+1):
            t = lst[i][j:j+N]
    
            for k in range(len(t)//2):
                if t[k] != t[len(t)-k-1]:
                    break
            else:
                cnt += 1
    return cnt 

for tc in range(1,11):

    N = int(input())
    case = [input() for _ in range(8)]

    cntV = pal(case,N) + pal(turn_list(case),N)

    print(f'#{tc} {cntV}')