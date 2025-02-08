# 백준 14916 - 거스름돈

n = int(input())

found = False
for i in range(n // 2 + 1) :
    if (n - 2 * i) % 5 == 0 :
        print(i + (n - 2 * i) // 5)
        found = True
        break

if not found :
    print(-1)