from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    friend_index = {friend: i for i, friend in enumerate(friends)}

    # 1. 주고받은 선물 기록을 행렬로 저장
    gift_map = [[0] * n for _ in range(n)]
    send_count = [0] * n
    receive_count = [0] * n

    for gift in gifts:
        sender, receiver = gift.split()
        s_idx, r_idx = friend_index[sender], friend_index[receiver]
        gift_map[s_idx][r_idx] += 1
        send_count[s_idx] += 1
        receive_count[r_idx] += 1

    # 2. 선물 지수 계산
    gift_index = [send_count[i] - receive_count[i] for i in range(n)]

    # 3. 다음 달 선물 주고받기 시뮬레이션
    next_gifts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                continue

            if gift_map[i][j] > gift_map[j][i]:  # i가 더 많이 줬다면 i가 받음
                next_gifts[i] += 1
            elif gift_map[i][j] < gift_map[j][i]:  # j가 더 많이 줬다면 j가 받음
                next_gifts[j] += 1
            else:  # 주고받은 수가 같다면 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    next_gifts[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_gifts[j] += 1

    # 4. 가장 많이 받을 선물 개수 반환
    return max(next_gifts)
