#code1
for tc in range(1,11):

    dump_num = int(input())
    dump_list = list(map(int,input().split()))
    # print(dump_list)

    for i in range(dump_num):
        maxN=0
        minN=101
        maxI=0
        minI=0

        for j in range(100):
            if dump_list[j] > maxN:
                maxI=j
                maxN = dump_list[j]
            if dump_list[j] < minN:
                minI=j
                minN = dump_list[j]
            
        maxN -= 1
        minN += 1
        dump_list[minI]=minN
        dump_list[maxI]=maxN

    if 0 <= maxN-minN <=1:
        print(maxN-minN)

    result= [0,100]
    for i in dump_list:
        if i > result[0]:
            result[0] = i
        if i < result[1]:
            result[1] = i
  
    print(f'#{tc} {result[0]-result[1]}')



    #code2
    # for tc in range(1,11):

    # dump_num = int(input())
    # dump_list = list(map(int,input().split()))

    # for i in range(dump_num): #덤프횟수만큼

    #     cnt = {'maxN' : 0, 'minN' : 101, 'maxI' : 0, 'minI' : 0} 
    #     # 가장 높음, 가장낮음, 가장높은것의 인덱스, 가장 낮은 것의 인덱스
    #     for j in range(100):
    #         if dump_list[j] > cnt['maxN']: #가장 높은거 구하기
    #             cnt['maxI'] = j
    #             cnt['maxN'] = dump_list[j]
    #         if dump_list[j] < cnt['minN']: #가장낮은거 구하기
    #             cnt['minI'] = j
    #             cnt['minN'] = dump_list[j]
    #     # 가장 높은거 ==> 가장 낮은거로 덤프 , 덤프리스트 변한 값으로 바꾸기 
    #     cnt['maxN'] -= 1
    #     cnt['minN'] += 1
    #     dump_list[cnt['minI']] = cnt['minN']
    #     dump_list[cnt['maxI']] = cnt['maxN']

    # if 0 <= cnt['maxN']-cnt['minN'] <= 1: # 최대와 최소 차이가 0이나1일 때
    #     print(cnt['maxN']-cnt['minN'])
    # #덤프리스트 돌면서 최대최소 구하기
    # result = [0,100] #[최종 최대값, 최소값]
    # for i in dump_list:
    #     if i > result[0]:
    #         result[0] = i
    #     if i < result[1]:
    #         result[1] = i
  
    # print(f'#{tc} {result[0]-result[1]}')