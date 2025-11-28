a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
t = min(a/i, b/j, c/k)
print(a-i*t, b-j*t, c-k*t)