def solution(order):
    answer = 0
    a = list(str(order))

    for i in range(len(a)):
        if (int(a[i]) % 3 == 0) and int(a[i]) > 0:
            answer += 1

    return answer