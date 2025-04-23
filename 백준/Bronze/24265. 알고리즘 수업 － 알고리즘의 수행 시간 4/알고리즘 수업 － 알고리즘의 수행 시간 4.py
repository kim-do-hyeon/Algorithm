# 백준 24265 - 알고리즘 수업 - 알고리즘의 수행 시간 4
# 분류 : 시간복잡도

N = int(input())
print(int(N * (N - 1) - (N - 1) * N / 2))
print(2)

# def MenOfPassion(A, N) :
#     count = 0
#     sum = 0
#     for i in range(1, N - 1) :
#         for j in range(i + 1, N) :
#             sum = sum + A[i] * A[j]
#             count += 1
#     return sum, count