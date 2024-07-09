def solution(myStr):
    answer = []

    for i in myStr:
        if i == "a" or i == "b" or i == "c":
            myStr = myStr.replace(i, " ")
    answer = myStr.split()
    
    return answer