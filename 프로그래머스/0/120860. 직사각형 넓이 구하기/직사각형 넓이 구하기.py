def solution(dots):
    answer = 0

    x = max(dots)[0] - min(dots)[0]
    y = max(dots)[1] - min(dots)[1]

    answer = x * y
    return answer