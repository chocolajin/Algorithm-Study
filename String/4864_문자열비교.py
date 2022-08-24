#code1

def boyer(pattern,text,lenp,lent):
    i = lenp - 1
    j = lenp - 1
    while i < lent:
        if text[i] == pattern[j]:
            i -= 1
            j -= 1
        if text[i] != pattern[j]:
            for k in range (lenp-2,-1,-1):
                if pattern[k] == text[i]:
                    skip = lenp-k-1
                    break
            else:
                skip = lenp
            i += skip
            j = lenp - 1
        if j == 0 :
            return 1
    return 0
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = boyer(str1,str2,N,M)
    print(f'#{tc} {result}')



#code2
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    for i in range(M-N+1):
        for j in range(N):
            if str2[i+j] != str1[j]:
                break
        else: 
            print(f'#{tc} {1}')
            break
    else: print(f'#{tc} {0}')