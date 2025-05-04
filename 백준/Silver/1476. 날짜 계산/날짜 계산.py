# 백준 1476 - 날짜 계산
# 분류 : 코딩 테스트 준비 - 기초 ) 브루트 포스

E, S, M = map(int, input().split())
years = 1
e = s = m = 1

while True :
    if e == E and s == S and m == M :
        print(years)
        break
    years += 1
    e += 1
    s += 1
    m += 1

    if e > 15 :
        e = 1
    if s > 28 :
        s = 1
    if m > 19 :
        m = 1