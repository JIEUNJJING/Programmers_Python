def solution(numbers, n):
    answer = 0
    sum = 0

    for i in numbers:
        sum += i
        if (sum > n):
            answer = sum
            return answer
    return answer