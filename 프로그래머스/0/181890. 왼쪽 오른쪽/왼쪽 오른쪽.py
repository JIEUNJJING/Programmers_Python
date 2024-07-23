def solution(str_list):
    answer = []

    for i in str_list:
        if i == 'l':
            answer = str_list[0:str_list.index(i)]
            break
        elif i == 'r':
            answer = str_list[str_list.index(i) + 1:]
            break
        else:
            answer = []

    return answer