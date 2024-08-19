def solution(nums):
    answer = 0
    mon =[] # 서로다른 폰캣몬 종류를 담는 리스트

    for i in nums: # nums 내 숫자 반복
        if len(mon) < len(nums) // 2 and i not in mon: # mon(서로다른 폰캣몬을 담는)리스트 길이가 N/2보다 작고, mon 리스트에 i(폰캣몬)가 없는 경우
            mon.append(i) # 폰캣몬 추가
        answer = len(mon) # 길이 반환
    return answer