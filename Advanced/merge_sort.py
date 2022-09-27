#굳이 안만들어도 되지만..깔끔하니까
def merge(left, right):    #정렬된 리스트 두 개 받아서 정렬된하나의 리스트를 만드는 함수
    result = []
    while left and right:   # 둘 다 요소가 있을 때
        # 각각 가장 앞쪽 값 확인후 작은값 빼주기
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 남아있는 요소 뒤에 붙여주기
    if left:
        result += left
    if right:
        result += right
    return result

# Merge Sort
# 1. 전체를 정렬하기 위해서 절반으로 나눈다
#   단 요소가 하나라면, 그대로 반환
# 2. 각 절반(left, right)를 정렬하고, 둘을 합친다(merge).
def merge_sort(lst):   #리스트를 받아서 정렬해서 반환하는 함수
    # 길이 1은 정렬할 필요가 없으니 그냥 반환
    N = len(lst)
    if N == 1:
        return lst
    m = N // 2
    left = lst[:m]
    right = lst[m:]
    left = merge_sort(left)  # 왼쪽 절반 정렬
    right = merge_sort(right)   # 오른쪽 절반 정렬
    return merge(left, right)    # 합치기

arr = [5,4,3,2,1]
result = merge_sort(arr)
print(result)
