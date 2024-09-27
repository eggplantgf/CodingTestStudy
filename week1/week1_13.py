# 피자 나눠먹기 (1)

def solution(n):
    if n%7 != 0 :
        return n//7 +1
    else:
        return n//7