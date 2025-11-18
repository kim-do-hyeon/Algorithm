import sys


def hamming_distance(a, b):
    """두 단어 a, b 사이의 다른 글자 개수를 센다."""
    length = len(a)
    diff_count = 0

    i = 0
    while i < length:
        if a[i] != b[i]:
            diff_count += 1
        i += 1

    return diff_count


def main():
    input = sys.stdin.readline

    first_line = input().strip()
    if first_line == "":
        return

    t = int(first_line)  # 테스트 케이스 개수

    case_index = 0
    while case_index < t:
        # 사샤가 말한 단어
        word = input().strip()
        while word == "":
            word = input().strip()

        # 사전 단어 개수
        w_line = input().strip()
        while w_line == "":
            w_line = input().strip()
        w = int(w_line)

        best_word = None
        best_distance = None

        count = 0
        while count < w:
            candidate = input().strip()
            # 혹시 빈 줄이 끼어 있으면 무시하고 다시 읽기
            if candidate == "":
                continue

            d = hamming_distance(word, candidate)

            # 첫 단어나, 더 적은 차이가 나는 단어로 갱신
            if best_distance is None or d < best_distance:
                best_distance = d
                best_word = candidate

            # 같은 거리일 때는 "사전에 먼저 등장한 단어"가 더 우선이므로
            # 나중에 나온 단어는 무시하면 됨 (따로 처리 필요 없음)
            count += 1

        sys.stdout.write(best_word + "\n")
        case_index += 1


if __name__ == "__main__":
    main()
