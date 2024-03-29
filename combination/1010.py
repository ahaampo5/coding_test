# 다리 놓기
# 21.07.01
# / 연산에서 예외 발생 - 해결하려면 반올림해
# import sys
# input = sys.stdin.readline
# t = int(input())

# answer = []
# for _ in range(t):
#     n, m = map(int,input().split())
#     a = 1
#     for i in range(m,m-n,-1):
#         a *= i
#     for j in range(1,n+1):
#         a //= j
#     answer.append(a)

# for ans in answer:
#     print(ans)

import sys, math
input = sys.stdin.readline

n = int(input().rstrip())

answer = []
for i in range(n):
    left, right = map(int, input().split())
    # right C left
    combination = math.factorial(right)// \
        math.factorial(right-left) // math.factorial(left)
    answer.append(combination)

for ans in answer:
    print(ans)