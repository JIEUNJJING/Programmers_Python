def solution(polynomial):
    answer = ''
    numberlist = polynomial.split()
    x = 0 # x계수
    s = 0 # 상수 

    for i in numberlist:
        if i[-1] == 'x': # i의 끝 글자가 'x'라면
            if i[:-1]: # 'x' 앞 숫자(계수)가 있다면
                x += int(i[:-1]) # x 변수에 계수 값 더해주기
            else: # 'x' 앞 숫자(계수)가 없다면
                x += 1 # 계수 값은 1을 나타내므로 1 더해줌
        elif i.isdigit(): # 상수일 경우
            s += int(i) # 상수값을 더해주는 변수 s에 더해줌

    if x == 1: # x 계수가 1인경우 출력
        if s > 0: # 상수항이 있는 경우
            answer = f"x + {s}"
        else: # 상수항이 없는 경우
            answer = f"x"
    elif x > 1: # x계수가 1보다 크고
        if s > 0: # 상수항이 있는 경우
            answer = f"{x}x + {s}"
        else: # 상수항이 없는 경우
            answer = f"{x}x"
    else: # 상수항만 있는 경우
        answer = f"{s}"
    return answer