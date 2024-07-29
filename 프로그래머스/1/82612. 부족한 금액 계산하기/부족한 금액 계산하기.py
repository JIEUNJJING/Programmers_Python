def solution(price, money, count):
    answer = -1
    cnt = 1 # 몇번탔는지 알려주는 함수
    sum = 0 # N번 이용할 경우 이용료의 N배해서 더한 값 넣어주는 변수

    while(cnt <= count): # count번까지 반복
        sum += price * cnt # N번 이용할 경우 이용료의 N배
        cnt += 1 

    if sum > money:
        answer = abs(sum - money)
    else:
        answer = 0

    return answer