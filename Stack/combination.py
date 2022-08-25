# 호출 마다 idx의 요소가 조합에 포함되는지 결정
# 선택된 요소의 개수를 알고 있어야 한다.
# 조합은 개수가 정해져 있어서...
# K : 여태까지 선택된 요소의 개수
def combination(idx,K,selected):
    if K == M:  # M개 만큼 요소 선택 끝남
        print(selected)
        return
    # 인덱스 검사는 끝났는데, 요소 선택이 덜 됨..
    if idx == N:    
        # 우리가 원하는 결과가 아니니.. 아무작업 하지 않음
        return
    selected[idx] = 1
    combination(idx + 1, K + 1,selected)
    selected[idx] = 0
    combination(idx + 1, K , selected)
arr = [1,2,3,4,5]
N = 5
M = 3
combination(0,0,[0]*N)