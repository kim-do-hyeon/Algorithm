# 백준 1924 - 2007년
# 분류 : 시뮬레이션

months = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())
current = sum(months[i] for i in range(1, x))
current += y
print(days[(current - 1) % 7])