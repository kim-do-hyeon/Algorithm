# 백준 14215 - 세 막대
# 단계별로 풀어보기 - 10 기하: 직사각형과 삼각형
# 분류 : 수학

A, B, C = sorted(map(int, input().split()))

if A + B <= C :
    C = A + B - 1
print(A + B + C)