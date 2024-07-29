def solution(phone_number):
    answer = ''

    phone_number = list(phone_number) # 문자열을 리스트로 변환
    for i in range(len(phone_number) - 4): # 마지막 4자리를 제외한 나머지 7자리 반복
        phone_number[i] = '*' # '*'로 바꿔주기
    answer = "".join(phone_number) # 다시 문자열로 변환
    return answer