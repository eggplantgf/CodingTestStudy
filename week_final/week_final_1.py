# 저주의 숫자 3

def solution(n):
    cnt = 0
    for i in range(n):
        cnt += 1
        # while을 조건문처럼
        while cnt%3 == 0 or "3" in str(cnt):
            cnt += 1
            
    return cnt