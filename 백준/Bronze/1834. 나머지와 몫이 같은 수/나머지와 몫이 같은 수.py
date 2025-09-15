# [브론즈 1] 백준 1834 - 나머지와 몫이 같은 수

N = int(input())
result = 0
for i in range(1, N) :
    result += N * i + i
print(result)