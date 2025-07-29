# 백준 5565 - 영수증

cost = int(input())
for i in range(9) :
    cost -= int(input())

print(cost)