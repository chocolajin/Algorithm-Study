def sdo(puzzle):
    for i in range(9):
        C = [0] * 10
        for j in range(9):
            if C[puzzle[i][j]] == 0:
                C[puzzle[i][j]] += 1
            else:
                return False
    else: return True

def rowP(puzzle):
    row_puzzle = [[]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            row_puzzle[i] += [puzzle[j][i]]
    return row_puzzle

def squP(puzzle):
    squ_puzzle = [[] for _ in range(9)]

    idx = 0

    for k in range(0,9,3):
        for l in range(0,9,3):
            for i in range(3):
                for j in range(3):
                    squ_puzzle[idx].append(puzzle[k + i][l + j])
            idx += 1
    return squ_puzzle

T = int(input())

for tc in range(1,T+1):
    puzzle = [list(map(int,input().split())) for _ in range(9)]
    # print(puzzle)
    # print(sdo(puzzle))
    if sdo(puzzle) and sdo(rowP(puzzle)) and sdo(squP(puzzle)):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
