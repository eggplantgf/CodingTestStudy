# 문자열 정렬하기 (1)

def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= 48 and ord(i) <= 57:
            answer.append(int(i))
    answer.sort()
    return answer