# 순서쌍의 개수

def solution(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0 and n != i*i :
            cnt += 2
        elif n == i*i :
            cnt += 1
        else:
            pass
    return cnt