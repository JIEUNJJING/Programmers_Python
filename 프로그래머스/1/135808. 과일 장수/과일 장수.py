def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True) # 사과 점수를 내림차순으로 정렬하여 가장 높은 점수부터 처리
    i = 0
    while (i + m <= len(score)): # 현재 i에 m을 더했을 때, score길이를 넘지 않는다면 (상자를 만들 수 있을 만큼의 사과가 남아있음을 의미)
        box = score[i : i + m]
        answer += min(box) * len(box) # 상자에 담긴 사과의 최소 점수 * 상자의 크기(m)
        i += m # 다음 상자를 만들기 위해 인덱스를 m만큼 더해줌
        
    return answer