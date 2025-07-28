# 백준 1408 - 24
# 분류 : 구현

current = list(map(int, input().split(":")))
finish = list(map(int, input().split(":")))

current_time = current[0] * 3600 + current[1] * 60 + current[2]
finish_time = finish[0] * 3600 + finish[1] * 60 + finish[2]

calc_time = (finish_time - current_time)
if calc_time < 0 :
    calc_time += 86400
hour = calc_time // 3600
calc_time %= 3600
minute = calc_time // 60
calc_time %= 60
seconds = calc_time
print(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(seconds).zfill(2)}")