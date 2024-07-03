def solution(my_string, letter):
    answer = ''
    a = list(my_string)

    for i in range(len(a)):
        if letter != my_string[i]:
            answer += my_string[i]

    return answer