def solution(n, k):
    answer = []

    for i in range(n + 1):
        if (1 <= i <=n) and (i % k == 0):
            answer.append(i)
    answer.sort()

    return answer