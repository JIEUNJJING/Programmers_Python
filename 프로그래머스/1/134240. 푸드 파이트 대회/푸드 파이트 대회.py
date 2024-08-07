def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2) # 문자열 곱셈은 문자(str(i))를 (food[i] // 2)번 출력해줌 
    return answer + '0' + answer[::-1]