def solution(arr):
    answer = []
    row = len(arr)
    col = len(arr[0])
    
    if row > col: # 행의 수가 더 클 경우
        for i in arr:
            answer.append(i + [0]* (row - col)) # 각 열 원소 그대로 넣어주고 0을 추가해 길이 맞추기
    elif row < col: # 열의 수가 더 클 경우
        answer = arr # answer에 arr 원소들을 넣어준 후
        for i in range(col - row): # 열에서 행의 수를 뺀 값만큼
            answer.append([0] * (col)) # 0 추가해주기
    else: # 길이 같을 경우
        answer = arr 
    return answer