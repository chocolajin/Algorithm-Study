# 카운팅 정렬
arr = [2, 4, 1, 7, 6, 2, 7, 8, 3, 1, 6, 15]
# 1. 각 요소가 몇 번 나오는지 숫자세고
# 2. 각 숫자가 나온 개수를 누적합 구하기(내가 몇번째냐? 구하기)
# 3. 원래 배열 확인하면서, 각 자리에 맞게 넣어주기

N = 12  # 배열 길이
K = 15  # 요소 최대값

# 1번 : 값을 인덱스로 활용
counts = [0] * (K+1)   # 최대값이 15니까 16개짜리 만들어서 15번 인덱스도 사용
for i in range(N):
    # arr[i] 가 나오면,   예) 3이 나오면, counts 배열의 3번인덱스 값을 1증가
    # counts 배열의 arr[i]번째 요소를 1증가
    counts[arr[i]] += 1
# 2번
for i in range(1, K+1):  #0번요소는 앞요소가 없음!
    # 앞요소 값을, 내 요소값이랑 더해서 저장
    # counts[i] = counts[i] + counts[i-1]
    counts[i] += counts[i-1]
# 3번   >>> 정렬될 위치에 넣어주면 되는데...새로운 배열 만들어서 복사
new_arr = [-1] * N  # -1은 의미없음!
for i in range(N):
    #arr[i] 가 들어갈 위치는 counts가 알고 있음 counts[arr[i]]
    counts[arr[i]] -= 1
    new_arr[counts[arr[i]]] = arr[i]

print(arr)
print(new_arr)

