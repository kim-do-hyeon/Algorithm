# [브론즈 3] 백준 2991 - 사나운 개
A, B, C, D = map(int, input().split())
li = list(map(int, input().split()))
for n in li:
    attacked = 0
    if 0 < n % (A+B) <= A:
        attacked += 1
    if 0 < n % (C+D) <= C:
        attacked += 1
    print(attacked)