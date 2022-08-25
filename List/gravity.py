T = int(input())

for tc in range(1,T+1):
    N = int(input())
    # room = input().split()
    room = list(map(int, input().split()))
    # 각 테스트 케이스별 문제 풀이
    # 가장 많이 떨어지는 상자의 낙차는 가장 왼쪽 상자도 아니고, 가장 높은상자도 아님
    # 각 열에서 가장 높이있는 상자가 떨어지는 낙차를 구하고, 그 중에서 가장 큰 낙차를
    # 출력하면 되는 문제
    # 낙차를 구하는 방법????
    # 0번 열의 낙차를 구해봅시다.
    # 1번열 부터 N-1번열 까지 반복
    
    
    #0번 열의 낙차 구하는 작업
    # 0번~N-2열 까지 구하도록.. 변경
    # cnt중에서 제일 큰 값을 저장하기 위한 변수가 필요
    # 제일 큰 값을 넣기 위한 변수 선언...큰값을 넣고 싶을 때는
    # 초기화는 최대한 작은 수를 넣어줍니다.
    result = 0
    for j in range(0, N-1):
        cnt = 0
        for i in range(j+1, N):
            if room[i] < room[j]:
                cnt += 1
        # print(cnt)  # 나는 ....cnt 들 중에 제일 큰 cnt 뽑고 싶음
        # 출력이 아니라...제일 큰지 제일 크면 저장
        if cnt > result:
            result = cnt


    # # 정답 출력  >>> #1 정답
    # result = 0
    print(f'#{tc} {result}')