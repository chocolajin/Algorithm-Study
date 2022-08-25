# 행마다 하나의 퀸을 놓을거고
# 모든 행에서 모든 열에 퀸 놓아보기
def nq(row,position):
    if row == N: # 모든 행에 퀸을 다 놓아보고 범위를 벗어남
        print(position)
    # row : 어떤 행에 퀸을 놓고 있는지 표시하는 변수
        return 1
    result = 0
    for col in range(N):  # (row,col)
        # col 열에 퀸 놓아보기
        # 가능성이 없는 경우의수를 수행하지 않는다.
        if check_col[col] or check_dia1[row + col] or check_dia2[row - col + N - 1]:
            continue
        check_col[col] += 1
        check_dia1[row + col] += 1
        check_dia2[row - col + N - 1] += 1
        position.append((row,col))
        result += nq(row + 1,position)  # 다음행에 퀸놓으러 가기
        position.pop()
        # 원래대로 되돌려 놓기
        check_col[col] -= 1
        check_dia1[row + col] -= 1
        check_dia2[row - col + N - 1] -= 1
    return result
N = 8
# board = [[0]*N for _ in range(N)]
#열에 퀸을 놓을수 있는지 검사 >>> N개 짜리 배열
check_col = [0] * N
# 대각선의 개수 >>> 2 * N - 1
# 대각선1 : 왼쪽 아래쪽으로 내려가는 대각선 검사
# 대각선1의 사용가능 여부를 표시하는 배열의 인덱스 : r+c
# 대각선2 : 오른쪽 아래쪽으로 내려가는 대각선 검사
# 대각선2의 사용가능 여부를 표시하는 배열의 인덱스 : r-c+(N-1)
check_dia1 = [0] *(2 * N - 1)
check_dia2 = [0] *(2 * N - 1)

print(nq(0,[]))


