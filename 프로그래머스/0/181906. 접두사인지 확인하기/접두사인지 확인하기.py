def solution(my_string, is_prefix):
    answer = 0
    a = ""

    for i in range(len(my_string)):
        a += my_string[i]
        print(a)
        if a == is_prefix:
            answer = 1
            return answer
        else:
            answer = 0

    return answer