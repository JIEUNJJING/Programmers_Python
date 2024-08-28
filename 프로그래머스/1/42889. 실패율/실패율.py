def solution(N, stages):
    answer = []
    p = {} # 각 스테이지에 머물러 있는 플레이어 수를 저장할 딕셔너리
    f = {} # 각 스테이지의 실패율을 저장할 딕셔너리
    player_num = len(stages)

    # 각 스테이지에 머물러 있는 플레이어 수 계산
    for i in stages:
        if i not in p:
            p[i] = 1 # 처음 등장하는 스테이지는 1로 초기화
        else:
            p[i] += 1 # 이미 등장한 스테이지는 1씩 증가

    # 실패율 계산 (각 스테이지 별로 실패율이 계산되어야 한다.)
    for i in range(1, N + 1): # 1 - 5 스테이지까지 반복
        if i in p: # i(스테이지) 가 p 에 포함되어 있을때 실패율 계산
            f[i] = p[i] / player_num
            player_num -= p[i]
        else:
            f[i] = 0 # 스테이지가 스테이지 번호 테이블에 없을때 실패율은 0 이다.

    a = sorted(f.items(), key=lambda x:x[1], reverse=True) # 실패율을 내림차순으로 정렬

    # 실패율 딕셔너리에서 스테이지 번호만 리턴
    for i in a:
        answer.append(i[0])
            
    return answer