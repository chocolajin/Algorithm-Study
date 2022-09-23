#code1
def solve_2(k):
    for i in range(k):
        for j in ['0', '1']:
            n2 = num2[:]
            n2[i] = j
            num2_set.update([int(''.join(n2), 2)])

def solve_3(k):
    for i in range(k):
        for j in ['0', '1', '2']:
            n3 = num3[:]
            n3[i] = j
            num3_set.update([int(''.join(n3), 3)])
    pass

T = int(input())
for tc in range(1, T+1):
    num2 = list(input())
    num3 = list(input())
    num2_set = set()
    num3_set = set()
    solve_2(len(num2))
    solve_3(len(num3))

    result = num2_set&num3_set
    print(f'#{tc}', end=' ')
    print(*result)