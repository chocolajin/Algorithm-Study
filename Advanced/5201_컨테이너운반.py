#code1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)

    result = []
    try:
        for i in range(M):
            for j in range(N):
                if t[i] >= w[j]:
                    result.append(w[j])
                    del w[j]
                    break
    except:
        pass

    print(f'#{tc} {sum(result)}')




#code2
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    wi =list(map(int,input().split()))
    ti = list(map(int,input().split()))
    result = 0
    while wi and ti:
        max_wi = max(wi)
        max_ti = max(ti)
        # wi 에서 최대 값을 뽑아서
        if max_wi <= max_ti:
        # 그 wi 최대 값 <= ti 최대값인 경우 지정한 변수 result에 + wi 최댓값
            result +=max_wi
            wi.remove(max_wi)
            ti.remove(max_ti)
        else:
            wi.remove(max_wi)
    print(f'#{tc} {result}')
    # 그리고 리스트에서 최대 값 삭제
    # 만약 wi 최대값 > ti 최대값 인 경우
    # wi 최대값 삭제
    # wi가 빈리스트가 되는 경우에 while문 탈출 하고 result 값 출력