def solution(bin1, bin2):
    answer = ''
    num1 = int(bin1, 2) # 2진수 문자열을 10진수 정수로 변환
    num2 = int(bin2, 2)
    sum = num1 + num2 

    answer = bin(sum).replace("0b", "") # 10 진수를 이진수로 변환 후, 0b 제거
    
    return answer