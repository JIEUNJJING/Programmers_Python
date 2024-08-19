def solution(a, b):
    answer = ''
    days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED'] # days[1] : 금요일 
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31] # 1 - 12월 일 수
    day = 0 # 모든 날짜를 더해 담아주는 변수

    for i in range(a - 1): # 구하는 월 전에 월까지 일 수를 더해줌
        day += months[i]
    day += b # 구하는 월의 일 수를 더해줌

    answer = days[day % 7] # 다 더해준 후 7로 나눈 나머지 구하면 요일을 찾을 수 있음

    return answer