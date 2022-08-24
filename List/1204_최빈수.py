T = int(input())
for tc in range(1,T+1):
    case_num = int(input())
    grade_list = list(map(int,input().split()))
    cnt = [0]*101
    for i in range(1000):
        cnt[grade_list[i]] += 1
    maxN = 0
    maxI = 0
    for i in range(101):
        if cnt[i] >= maxN:
            maxN = cnt[i]
            maxI = i
    print(f'#{tc} {maxI}')
