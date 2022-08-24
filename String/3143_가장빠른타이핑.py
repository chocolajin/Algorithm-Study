T = int(input())
for tc in range(1, T+1):
    A, B = input().split()


    cnt = 0
    i = 0
    while i < len(A)-len(B)+1:
        for j in range(len(B)):
            if A[i+j] != B[j]:
                i += 1
                break
        else:
            cnt += 1
            i += len(B)


    print(f'#{tc} {len(A)-len(B)*cnt+cnt}')