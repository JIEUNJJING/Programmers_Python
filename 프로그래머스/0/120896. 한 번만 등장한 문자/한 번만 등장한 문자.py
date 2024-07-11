def solution(s):
    answer = ''
    a = []

    for i in s:
        if s.count(i) == 1:
            a.append(i) 
    a.sort()
    a = "".join(a)
    answer = a
    return answer