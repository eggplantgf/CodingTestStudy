# 카드 2 

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque([i for i in range(1,n+1)])

while len(arr) > 1:
    arr.popleft()
    card = arr.popleft()
    arr.append(card)
    
print(arr[0])

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [i for i in range(1,n+1)]
# i=0

# while i<n:
#     del arr[0]
#     i += 1
#     arr.append(arr[0])
#     i += 1

# print(arr[0])