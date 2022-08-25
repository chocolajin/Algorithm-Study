T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0,0,0,0,0
    while True:
        if N % 2:
            break
        else:
            N = N // 2
            a += 1
    while True:
        if N % 3:
            break
        else:
            N = N // 3
            b += 1
    while True:
        if N % 5:
            break
        else:
            N = N // 5
            c += 1
    while True:
        if N % 7:
            break
        else:
            N = N // 7
            d += 1
    while True:
        if N % 11:
            break
        else:
            N = N // 11
            e += 1
    print(f'#{tc} {a} {b} {c} {d} {e}')



#code2
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = [2, 3, 5, 7, 11]                      #나눠줄 숫자들
    res = [0] * 5                               #a~e를 저장할 배열

    for i in range(len(num)):
        while True:
            if N % num[i] == 0:                 #나누어 떨어지면 == 나머지가 없으면
                N = N // num[i]                 #그 값으로 N을 나눠주고
                res[i] += 1                     #res에 1 추가 해줌
            else:                               #나누어 떨어지지 않으면
                break                           #반복문 탈출하여 다음 수로 나누어줄 준비

    print(f'#{tc} {" ".join(map(str, res))}')   #출력할 때 띄어쓰기 넣어줘야 하므로 res의 모든 값을 str로 바꾼 후 join