T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    str_dict = {str:0 for str in str1}

    for i in range(M):
        for key in str_dict.keys():
            if str2[i] == key :
                str_dict[key] += 1
    maxV = 0        
    for value in str_dict.values():
        if value > maxV:
            maxV = value

    print(f'#{tc} {maxV}')