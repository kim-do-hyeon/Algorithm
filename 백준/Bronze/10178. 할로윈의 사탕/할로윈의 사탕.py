# 백준 10178 - 할로윈의 사탕

T = int(input())
for _ in range(T) :
    c, v = map(int, input().split())
    print(f"You get {c // v} piece(s) and your dad gets {c % v} piece(s).")