# 최댓값 만들기 (1)

def solution(numbers):
    numbers.sort()
    return numbers.pop() * numbers.pop()