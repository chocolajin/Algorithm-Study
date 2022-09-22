#code1

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






#code2
# 1. data내에서 암호코드 찾기
#    암호코드는 항상 1로 끝이나니까..뒤에서 부터 찾기
# 2. 2진으로 표현된 암호코드를 10진수로 변경하기
#    2진 암호코드 모양과 숫자를 연결해주는 dictionary 만들기
# 3. 8자리 암호가 정상 암호인지 아닌지 판별
# 4. 결과 출력
code_dic = {
(3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9
}



def solve():
    # 2진 암호 코드 찾기
    result = 0
    for i in range(N):
        for j in range(M-1,54,-1):
            if data[i][j] == 1: # 암호 코드 찾음!
                # 암호코드 분석하기(패턴으로 숫자 만들기)
                # 7개 비트 * 8개 = 56
                code = []
                for _ in range(8):  #숫자가 8개니까 8번 반복
                    # 7개 비트가 어떻게 생겼는지 파악
                    # 개수로 모양 파악하기위해서 변수선언
                    n1 = n2 = n3 = n4 = 0
                    # 1 개수 세기
                    while data[i][j] == 1:
                        n4 += 1
                        j -= 1
                    # 0 개수 세기
                    while data[i][j] == 0:
                        n3 += 1
                        j -= 1
                    # 1 개수 세기
                    while data[i][j] == 1:
                        n2 += 1
                        j -= 1
                    # 0 개수 세기
                    n1 = 7 - n2 - n3 - n4
                    j -= n1
                    # print(code_dic[(n1,n2,n3,n4)], end=' ')
                    code.append(code_dic[(n1,n2,n3,n4)])
                # 숫자 8개 얻기 완료
                # 홀수자리 짝수자리
                #[7,6,5,4,3,2,1,0]
                odd_nums = code[1] + code[3] + code[5] + code[7]
                even_nums = code[0] + code[2] + code[4] + code[6]
                if (odd_nums*3+ even_nums) % 10 == 0:
                    result = odd_nums + even_nums
                return result    #일단은...0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')
