# 백준 9063 - 대지
# 단계별로 풀어보기 - 10 기하: 직사각형과 삼각형
# 분류 : 수학

N = int(input())
min_x, min_y, max_x, max_y = 10000, 10000, -10000, -10000
for i in range(N) :
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))