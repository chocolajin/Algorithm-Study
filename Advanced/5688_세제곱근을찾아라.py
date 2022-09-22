#code1

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    print(n**(1/3))

    if abs(n**(1/3)-round(n**(1/3))) < 1e-9:
        print(f'#{t} {int(round(n**(1/3)))}')
    else:
        print(f'#{t} -1')

#code2
arr = [0] * (10**6+1)
for x in range(len(arr)):
    arr[x] = x**3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    try:
        print(f'#{tc} {arr.index(N)}')
    except:
        print(f'#{tc} -1')