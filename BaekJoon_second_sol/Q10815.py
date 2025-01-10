# 숫자 카드
# 기존 방법 : 딕셔너리
# 2nd 방법 : 이진 탐색

import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split())) # 보유 카드
M = int(input())
arr2 = list(map(int,input().split())) # 체크할 카드

arr1.sort()
for check in arr2:
    low, high = 0, N-1  # arr1 이진 탐색 index

    exist = False
    while low <= high:
        mid = (low + high) // 2
        if arr1[mid] > check:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif arr1[mid] < check:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break

    print(1 if exist else 0, end=' ') # False면 1 (디폴트)