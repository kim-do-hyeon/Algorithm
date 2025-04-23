# 백준 24267 - 알고리즘 수업 - 알고리즘의 수행 시간 6
# 분류 : 시간복잡도

N = int(input())
# count = 0
# for i in range(1, N - 1) :
#     for j in range(i + 1, N) :
#         for k in range(j + 1, N + 1) :
#             count += 1
# print(count)
print(N * (N - 1) * (N - 2) // 6)
print(3)