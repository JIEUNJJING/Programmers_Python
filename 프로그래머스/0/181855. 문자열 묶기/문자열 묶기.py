def solution(strArr):
    answer = 0
    str_len_dict = {}

    for i in strArr:
        length = len(i)
        if length not in str_len_dict: # length가 str_len_dic에 없다면
            str_len_dict[length] = 1 # 1로 초기화
        else: # length가 str_len_dic에 있다면
            str_len_dict[length] += 1 # 개수 1증가
    answer = max(str_len_dict.values())

    return answer