def solution(name, yearning, photo):
    answer = []
    dic = {}

    dic = dict(zip(name, yearning)) # 딕셔너리로 묶어줌

    for i in photo: 
        sum = 0 # 총 합 초기화(각각의 사진의 합을 구해야하므로)
        for j in i:
            if j in dic:
                sum += dic[j] # 각 key값에 대응되는 값을 더해줌
        answer.append(sum)

    return answer