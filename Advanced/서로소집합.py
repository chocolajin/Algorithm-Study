# 서로소 집합
# 서로같은 집합인지 아닌지 확인하기 위해서 대표자라는 개념을 가진다
# 각 노드는 부모를 가지는데, 노드 스스로가 부모이면 집합의 대표다
N = 10  # 최대 노드 번호
parent = [x for x in range(0, N+1)] # 인덱스에 해당하는 노드 번호를 가지는 노드의 부모를 저장하는 배열

# 인자로 받은 노드의 대표번호 반환
def find_set(x):
    # 방법1
    # if x== parent[x]:
    #     return x
    # else:
    #     return find_set(parent[x])

    # 방법2
    while x != parent[x]:
        x = parent[x]
    return x

# 인자로 받은 두 노드의 집합을 합치기(대표자의 번호를 똑같이 만들어주기)
def union(x,y):
    # x의 대표자 번호를 y의 대표자로 만들기
    # y의 대표자 부모를 x의 대표자로 만들기
    parent[find_set(y)] = find_set(x)

# 인자로 받은 두 노드가 같은 집합이면 True, 아니면 False
def check_same_set(x,y):
    if find_set(x) == find_set(y):
        return True
    return False

union(1,2)
union(4,5)
union(1,4)
print(parent)
print(check_same_set(1,5))
