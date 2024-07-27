def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    
    s = s.lower()
    for i in s:
        if i == 'p':
            cnt_p += 1
        elif i == 'y':
            cnt_y += 1
    if ('p' not in s and 'y' not in s) or cnt_p == cnt_y:
        return True
    else:
        return False

    return answer