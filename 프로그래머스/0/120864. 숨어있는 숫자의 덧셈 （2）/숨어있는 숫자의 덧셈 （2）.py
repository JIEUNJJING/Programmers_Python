def solution(my_string):
    answer = 0

    for i in my_string:
        if i.isalpha(): # 문자라면
            my_string = my_string.replace(i, ' ') # 공백으로 대체하기
    my_string = my_string.split() # 공백 기준으로 분할해 리스트로 만들기
    
    # my_string 리스트의 요소를 int로 변환해 숫자들을 모두 더해줌
    answer = sum(map(int, my_string))

    return answer
