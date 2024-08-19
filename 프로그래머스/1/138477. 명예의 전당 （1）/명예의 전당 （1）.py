def solution(k, score):
    answer = []
    s = [] # 현재 순위권에 있는 점수를 저장할 리스트

    for i in score:
        if len(s) < k: # 순위권에 k개의 점수가 채워지지 않은 경우
            s.append(i)
        else:
            if i > s[-1]: # 현재 점수가 순위권의 가장 낮은 점수보다 높은 경우
                s.pop(-1) # 마지막 값(가장 낮은 점수)을 제거
                s.append(i) # 새로운 점수 추가
        s.sort(reverse=True) # 내림차순 정렬 
        answer.append(s[-1]) # 가장 낮은 점수 answer에 추가

    return answer