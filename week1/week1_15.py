# 피자 나눠먹기 (3)

def solution(slice, n):
    if n%slice != 0:
        return n//slice + 1
    else:
        return n//slice