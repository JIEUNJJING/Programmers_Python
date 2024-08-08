def solution(cards1, cards2, goal):
    answer = "Yes"
    
    for i in goal:
        if i in cards1: # cards1에 있는 경우
            if i == cards1[0]: # 젤 앞에 값과 같으면 
                cards1.pop(0) # cards1에서 삭제
            else: # 다르면
                answer = "No" # "No" 반환 후 종료
                break
        elif i in cards2: # cards2에 있는 경우
            if i == cards2[0]:
                cards2.pop(0)
            else:
                answer = "No"
                break

    return answer