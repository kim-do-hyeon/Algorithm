# 백준 1075 - 나누기

N = int(input())
F = int(input())

divde = N // 100
answer = divde * 100

while answer % F != 0 :
    answer += 1
print(str(answer)[-2:])