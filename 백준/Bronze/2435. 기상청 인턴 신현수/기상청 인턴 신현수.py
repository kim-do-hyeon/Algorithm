n, k = map(int, input().split())
temp_li = list(map(int, input().split()))
total_temp = []
for i in range(n - k + 1):
    total = 0
    for j in range(i, i + k):
        total += temp_li[j]
    total_temp.append(total)
print(max(total_temp))