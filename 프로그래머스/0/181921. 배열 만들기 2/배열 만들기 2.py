def solution(l, r):
    answer = []
    num_list = []

    bin_max = 1 << len(str(r)) # 2진수 최대 자리수로 표현할 수 있는 수 + 1을 구한다.

    #for반복문은 bin_max-1 만큼 반복합니다.(그래서 위에서 +1한 값을 그대로 사용하면 됩니다.)
    for i in range(bin_max): 
        val = int(format(i, 'b').replace('1', '5')) # 2진수로 변환해준 후, 1을 5로 치환해줌

        if val >= l and val <= r: # 매개변수 l, r 범위에 속하면 num_list 에 추가한다.
            num_list.append(val)

    if len(num_list) == 0: # num_list 에 아무값도 없으면 -1을 answer 변수에 넣어준다.
        answer.append(-1)
    else:
        answer = sorted(num_list) # 오름차순으로 정렬하여 answer 변수에 넣어준다.
        
    return answer