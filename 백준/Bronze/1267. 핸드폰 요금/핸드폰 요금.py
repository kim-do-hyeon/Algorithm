# 백준 1267 - 핸드폰 요금

N = int(input())
A = list(map(int, input().split()))

y_cost = m_cost = 0

for i in A :
    y_cost += (i // 30 + 1) * 10
    m_cost += (i // 60 + 1) * 15

if y_cost == m_cost :
    print("Y M", m_cost)
elif m_cost < y_cost :
    print("M", m_cost)
else :
    print("Y", y_cost)