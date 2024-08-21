def solution(answers):
    answer = []
    s1 = [1,2,3,4,5] # 학생 1
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] # 학생 2
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 학생 3
    s1_sum = 0 # 학생 1의 정답 맞힌 수
    s2_sum = 0
    s3_sum = 0

    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]: # 학생 1의 패턴 반복 
            s1_sum += 1
        if answers[i] == s2[i % len(s2)]:
            s2_sum += 1
        if answers[i] == s3[i % len(s3)]:
            s3_sum += 1

    max_score = max(s1_sum, s2_sum, s3_sum) # 최대 값 구하기

    if s1_sum == max_score: # 최고점수와 학생1 점수가 같다면
        answer.append(1) # 1 추가
    if s2_sum == max_score:
        answer.append(2)
    if s3_sum == max_score:
        answer.append(3)

    return answer