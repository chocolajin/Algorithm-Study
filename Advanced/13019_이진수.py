#code1
to_num = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def binary(n):
    bi_num = ''
    for i in range(3, -1, -1):  # 16진수 1자리는 2진수 4자리로 표현된다
        bi_num += '1' if int(n) & (1 << i) else '0'
    return bi_num


T = int(input())
for tc in range(1, T + 1):
    N, hexadecimal = input().split()  # 47FE
    num = ''
    for h in hexadecimal:  # 각 자리수를 이진수로 표시할거야!
        if h in to_num:  # 10~15로 변경해주는 과정
            h = to_num[h]
        num += binary(h)
    print(f'#{tc} {num}')




#code2
T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    result = ''
    for i in M:
        num = int(i, 16)
        output = ''
        for j in range(3,-1,-1):
            output += '1' if num & (1<<j) else '0'
        # print(output)
        result += output
    print(f'#{tc} {result}')