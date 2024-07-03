def solution(sides):
    answer = 0
    min = max = mid = sides[0]

    for i in range(1, len(sides)):
        if sides[i] < min:
            min = sides[i]
        if sides[i] > max:
            max = sides[i]
        if min < sides[i] < max:
            mid = sides[i]
    if max < min + mid:
        answer = 1
    else:
        answer = 2
        
    return answer