def solution(myString, pat):
    answer = ''
    end_idx = myString.rfind(pat)
    print(end_idx)

    if pat in myString:
        answer += myString[:end_idx + len(pat)]
    return answer