code = ['0001101', '0011001','0010011','0111101','0100011','0110001','0101111', '0111011','0110111','0001011']
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    code_data = [input() for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if code_data[i][j] == '1':
                code_line = code_data[i]
                break
    for k in range(M-1,0,-1):
        if code_line[k] == '1':
            code_realline = code_line[k-55:k+1]
            break   
    code_number = [0]*8
    for i in range(8):
        number = code_realline[7*i:7*(i+1)]
        for j in range(len(code)):
            if code[j] == number:
                code_number[i] = j
    def access_code(num):
        odd = 0
        even = 0
        for n in range(len(num)):
            if n % 2:
                odd += num[n]
            else: even += num[n]
        if (even*3 + odd) % 10:
            return 0
        else: return odd + even
    print(f'#{tc} {access_code(code_number)}')