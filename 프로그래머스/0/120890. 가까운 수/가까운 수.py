def solution(array, n):
    array.sort()
    answer = array[0]
    diff = abs(n - array[0])
    for i in array:
        if diff > abs(n - i):
            diff = abs(n - i)
            answer = i
    return answer