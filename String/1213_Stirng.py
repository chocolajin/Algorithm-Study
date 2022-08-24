for tc in range(1,11):
    T = input()
    pattern = input()
    text = input()

    cnt = 0
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            cnt += 1

    print(f'#{tc} {cnt}')