# 백준 2460 - 지능형 기차 2
# 분류 : 수학

count = 0
max_count = 0
for _ in range(10) :
    off, on = map(int, input().split())

    count -= off
    count += on
    max_count = max(max_count, count)

print(max_count)