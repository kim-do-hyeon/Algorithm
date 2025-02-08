# 백준 33277 - 국방시계
# 분류 : 사칙연산

N, M = map(int, input().split())

time_decimal = ((M / N) * 24)
hours_total = int(time_decimal)
minutes_fraction = time_decimal - hours_total
hours_24 = hours_total
minutes = int(minutes_fraction * 60)
print(f"{hours_24:02d}:{minutes:02d}")