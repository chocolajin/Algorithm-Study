for tc in range(1,11):

    T = int(input())
    case = [list(map(int, input().split())) for _ in range(100)]
    # print(case)
    # 마지막 줄에서 2를 찾아라! 마지막줄 = for i in rangr(100) if case(99,i)==2 start=i
    # <1>올라가 <2>만약 좌나 우로 길이 있으면(1이면) 글로가 좌우 없으면 위로가 <3>반복
    # 꼭대기 row 0 되면 그때 col 갑ㅅ은?

    for i in range(100):
        if case[99][i] == 2:
            cpoint = i
            rpoint = 98

            while rpoint != 0:

                if 0 <= cpoint+1 < 100 and case[rpoint][cpoint+1] == 1:
                    while cpoint+1 < 100 and case[rpoint][cpoint+1] != 0:
                        cpoint += 1

                elif 0 <= cpoint-1 < 100 and case[rpoint][cpoint-1] == 1:
                    while cpoint-1 >= 0 and case[rpoint][cpoint-1] != 0:
                        cpoint += -1

                rpoint += -1

    print(f'#{tc} {cpoint}')