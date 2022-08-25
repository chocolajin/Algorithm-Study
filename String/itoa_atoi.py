#itoa atoi
# atoi :
# 각 숫자형문자의 아스키코드에서 '0' 아스키 코드 번호 빼기
# 파이썬에서 문자의 아스키코드를 얻는 법: ord() 함수 사용
print(ord('1'))
#반대의 경우 48 >>> 코드에 해당하는 문자얻어오기 : chr()
print(chr(65))

def atoi(data):
    # data '123','12345'
    result = 0
    for i in range(len(data)):
        #현재인덱스 '문자'를 숫자로 변경
        num = ord(data[i]) - ord('0')
        result = result*10 + num
    return result
result = atoi('12345')
print(result, type(result))

def itoa(num):
    # 여기에 작성하시오. 40분 까지 작성해보세요!
    # 12345
    # 숫자를 10으로 나누고, 나머지를 문자열로 변경해서 저장
    # 몫은 다시 10으로 나눠서 나머지를 문자열로 변경하고 기존 결과와 더함 
    # 위 과정을 계속해서 반복함 >>> 몫이 0이 될 때 까지
    result = ''
    while num > 0:
        # 몫이 필요한게 아니라... 나머지가 필요
        remain = num % 10
        # remain + ord('0') remain의 아스키코드
        result = chr(remain + ord('0')) + result
        num = num // 10
    return result
result = itoa(456789)
print(result, type(result))











