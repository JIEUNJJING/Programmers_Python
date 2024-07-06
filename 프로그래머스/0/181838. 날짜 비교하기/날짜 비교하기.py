def solution(date1, date2):
    answer = 0

    for i in date1:
        for j in date2:
            if date1 < date2:
                answer = 1
            else:
                answer = 0
    return answer