# 백준 13909 - 창문 닫기
# 분류 : 수학

# N = int(input())

# A = [0 for _ in range(N)]
# for i in range(1, N + 1) :
#     for j in range(1, N + 1) :
#         if j % i == 0 :
#             if A[j - 1] == 0 :
#                 A[j - 1] = 1
#             else :
#                 A[j - 1] = 0

# print(A.count(1))

import math
N = int(input())
print(int(math.isqrt(N)))