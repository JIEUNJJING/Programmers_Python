def solution(names):
    answer = []
    i = 0

    for i in range(0, len(names), i + 5):
        answer.append(names[i])

    return answer