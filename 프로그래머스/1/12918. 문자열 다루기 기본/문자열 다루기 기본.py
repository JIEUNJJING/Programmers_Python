def solution(s):
    answer = True

    if s.isdigit() and (len(s) == 4 or len(s) == 6): # 숫자이고 길이가 4인지 확인
        answer = True
    else:
        answer = False
            
    return answer