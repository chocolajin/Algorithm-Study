import sys
sys.stdin = open('input.txt','r')

# code1 HELPHELPHELP
def baby(idx, k, card):
    if idx == k:
        print(card)
        if card[0] == card[1] and card[1] == card[2]:
            return 1
        if card[0]+1 == card[1] and card[1]+1 == card[2]:
            return 1
    else:
        for j in range(idx, k):
            card[idx], card[j] = card[j], card[idx]
            baby(idx+1, k, card)
            card[idx], card[j] = card[j], card[idx]

T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(6):
        player1.append(data[i*2])
        player1.sort()
        if len(player1) >= 3:
            winner = baby(0, len(player1), player1)
            if winner:
                print(f'#{tc} {1}')
                break

        player2.append(data[i*2+1])
        player2.sort()
        if len(player2) >= 3:
            winner = baby(0, len(player2), player2)
            if winner:
                print(f'#{tc} {2}')
                break
    else:
        print(f'#{tc} {0}')



#code2
#
# def baby(card):
#     i = 0
#     while i < 10:
#         if card[i] >= 3:
#             return True
#         if card[i]>=1 and card[i+1]>=1 and card[i+2]>=1:
#             return True
#         i+=1
#     return False
# T = int(input())
# for tc in range(1, T + 1):
#     data = list(map(int, input().split()))
#     player1 = [0]*12
#     player2 = [0]*12
#     for i in range(6):
#         player1[data[i*2]] += 1
#         if i >= 2:
#             winner = baby(player1)
#             if winner:
#                 print(f'#{tc} {1}')
#                 break
#
#         player2[data[i*2+1]] += 1
#         if i >= 2:
#             winner = baby(player2)
#             if winner:
#                 print(f'#{tc} {2}')
#                 break
#     else:
#         print(f'#{tc} {0}')
