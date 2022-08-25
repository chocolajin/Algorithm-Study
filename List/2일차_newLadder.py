# import sys
# sys.stdin = open('input.txt', 'r')
#
# for tc in range(1,11):
#
#     T = int(input())
#     case = [list(map(int, input().split())) for _ in range(100)]
# #     # print(case)
# #     # 마지막 줄에서 1을 찾아라! 마지막줄 = for i in rangr(100) if case(99,i)==1 start=i
# #     # <1>올라가 <2>만약 좌나 우로 길이 있으면(1이면) 글로가 좌우 없으면 위로가 <3>반복 갈 때마다 cnt+=1
# #     # 꼭대기 row 0 되면 그때 cnt값이 제일 작은 cpoint는?
#     minV = 10000
#     cpointV = 0
#     for i in range(100):
#         if case[99][i] == 1:
#             cpoint = i
#             rpoint = 98
#             cnt = 0
#             while rpoint != 0:
#
#                 if 0 <= cpoint+1 < 100 and case[rpoint][cpoint+1] == 1:
#                     while cpoint+1 < 100 and case[rpoint][cpoint+1] != 0:
#                         cpoint += 1
#                         cnt += 1
#
#                 elif 0 <= cpoint-1 < 100 and case[rpoint][cpoint-1] == 1:
#                     while cpoint-1 >= 0 and case[rpoint][cpoint-1] != 0:
#                         cpoint += -1
#                         cnt += 1
#
#                 rpoint += -1
#                 cnt += 1
#             if cnt < minV:
#                 minV = cnt
#                 cpointV = cpoint
#
#
#     print(f'#{tc} {cpointV}')



import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    T = int(input())
    case = [list(map(int, input().split())) for _ in range(100)]
    minV = 10000000
    cpointV = 0
    for i in range(100):
        if case[99][i] == 1:
            cpoint = i
            rpoint = 98
            cnt = 0
            while rpoint != 0:
                if 0 <= cpoint+1 < 100 and case[rpoint][cpoint+1] == 1:
                    while cpoint+1 < 100 and case[rpoint][cpoint+1] != 0:
                        cpoint += 1
                        cnt += 1
                elif 0 <= cpoint-1 < 100 and case[rpoint][cpoint-1] == 1:
                    while cpoint-1 >= 0 and case[rpoint][cpoint-1] != 0:
                        cpoint += -1
                        cnt += 1
                rpoint += -1
                cnt += 1
            if cnt < minV:
                minV = cnt
                cpointV = cpoint
    print(f'#{tc} {cpointV}')
