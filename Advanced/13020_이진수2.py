#code1
T = int(input())

for tc in range(1, T+1):
    N = float(input())

    result = ''
    for i in range(1, 13):
        N *= 2
        print(f'N : {N}')
        result += str(int(N) % 2)
        print(f'result : {result}')
        print()
        if N % 1 == 0:            # 정수로 딱 떨어지면
            break
    else:
        result = 'overflow'
    print(f'#{tc} {result}')





#code2
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = []
    while N % 1:
        result.append(int((N*2)//1))
        N = (N * 2)%1
        if len(result) >12:
            result=['overflow']
            break
    print(f'#{tc}',end=' ')
    print(*result, sep = '')
