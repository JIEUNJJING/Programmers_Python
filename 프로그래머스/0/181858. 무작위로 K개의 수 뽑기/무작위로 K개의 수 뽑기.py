def solution(arr, k):
    answer = []
    cnt = 0

    for i in arr:
        if i not in answer:
            answer.append(i)
            cnt += 1
            if cnt == k:
                break

    if len(answer) < k:
        answer = answer + ([-1] * (k - len(answer)))
    return answer