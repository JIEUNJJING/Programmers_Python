def solution(score):
    answer = []
    total = 0
    avg = 0
    score_avg = []
    rank = 1

    for i in score:
        total = 0
        for j in range(len(i)):
            total += i[j]
        avg = total / 2
        score_avg.append(avg)

    for i in score_avg:
        rank = 1
        for j in score_avg:
            if i < j:
                rank += 1
        answer.append(rank)

    return answer