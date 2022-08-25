cnt = 0

# 최대 N 이 200까지 들어올 수 있다.
memo = [0] * 201
# 메모이제이션 : 한 번 계산한 결과를 저장해두고 사용하는 것
def fibo(N):
    global cnt
    cnt += 1
    if N < 3:
        return 1
    if not memo[N]:
        memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

result = fibo(100)
print(f'cnt : {cnt} , result : {result}')


# 요소가 4개
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                print(i,j,k,l)
N = 6
select = [0] * N
def recursion(idx):
    if idx == N:
        print(select)
        return
    select[idx] = 0
    recursion(idx+1)
    select[idx] = 1
    recursion(idx+1)

recursion(0)




