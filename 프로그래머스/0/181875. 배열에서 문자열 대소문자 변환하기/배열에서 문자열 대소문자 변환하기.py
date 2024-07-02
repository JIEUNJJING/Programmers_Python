def solution(strArr):
    answer = []

    for i in range(len(strArr)):
        if i % 2 != 0: # 홀수번째 인덱스
            answer.append(strArr[i].upper())
        else: # 짝수번째 인덱스
            answer.append(strArr[i].lower())

    return answer