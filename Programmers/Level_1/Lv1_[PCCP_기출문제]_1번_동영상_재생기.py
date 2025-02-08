def total_seconds(time):
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds

def output(seconds):
    min = seconds // 60
    sec = seconds % 60
    return f"{str(min).zfill(2)}:{str(sec).zfill(2)}"

def solution(video_len, pos, op_start, op_end, commands):
    pos_time = total_seconds(pos)
    video_time = total_seconds(video_len)
    op_start_time = total_seconds(op_start)
    op_end_time = total_seconds(op_end)

    # **오프닝 구간 시작 시점에서 재생을 시작하면 바로 op_end로 이동**
    if op_start_time <= pos_time <= op_end_time:
        pos_time = op_end_time

    for cmd in commands:
        if cmd == "next":
            pos_time += 10
            if pos_time > video_time:  # 비디오 끝을 초과하면 마지막 위치로
                pos_time = video_time

        elif cmd == "prev":
            pos_time -= 10
            if pos_time < 0:  # 0초 이하로 내려가면 0초로 고정
                pos_time = 0

        # **오프닝 구간 체크 (이동 후에 확인)**
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time

    return output(pos_time)
