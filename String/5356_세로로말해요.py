T = int(input())
for tc in range(1, T+1):
    word = [input() for _ in range(5)]

    read_word = []
    for i in range(15):
        for j in range(5):
            try:
                read_word.append(word[j][i])
            except:
                pass
    print(f"#{tc}",end=' ')
    print(*read_word, sep = '')