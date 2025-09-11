# [브론즈 2] 백준 1668 - 트로피 진열

N = int(input())
A = [int(input()) for _ in range(N)]

left_current, right_current = 0, 0
left_max, right_max = 0, 0

for i in A :
    if i > left_max :
        left_max = i
        left_current += 1

for i in A[::-1] :
    if i > right_max :
        right_max = i
        right_current += 1

print(left_current)
print(right_current)