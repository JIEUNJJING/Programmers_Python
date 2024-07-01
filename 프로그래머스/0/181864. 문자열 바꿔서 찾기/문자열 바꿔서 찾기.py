def solution(myString, pat):
    answer = 0
    arr = []
    
    a = "".join(myString)

    for i in myString:
        if i == "A":
            arr += "B"
        else:
            arr += "A"

    c = "".join(arr)

    if pat in c:
        answer = 1
    else:
        answer = 0
            
    return answer