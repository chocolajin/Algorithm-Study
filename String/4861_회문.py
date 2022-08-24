#리스트 돌리는 함수
def turn_list(lst,n):
    new_list = [[]*n for _ in range(n)]
    for i in range(n):
        
        for j in range(n):
            new_list[i] += lst[j][i]    
    return new_list
           
#회문 검사 함수
def pal(lst,n,m):
    for i in range(n):
        for j in range(n-m+1):
            text = lst[i][j:j+m]

        for i in range(len(text)//2):
            if text[i] != text[len(text)-i-1]:
                break
        else:
            return text
    return False

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    case = [input() for _ in range(N)]
   
    if pal(case,N,M) != False:
        result = pal(case,N,M)
    else :
        result = ''.join(pal((turn_list(case,N)),N,M))
    
    print(f'#{tc} {result}')