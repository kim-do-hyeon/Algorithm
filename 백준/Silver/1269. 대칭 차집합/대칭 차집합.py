# 대칭 차집합

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_b = list(set(a) - set(b))
b_a = list(set(b) - set(a))
print(len(a_b) + len(b_a))